import os
from datetime import datetime
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ReadConfigurations
from selenium.webdriver.chrome.options import Options

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def setup(request):
    global driver
    browser = ReadConfigurations.read_configuration("basic info", "browser")

    if browser == 'chrome':
        # launch Chrome with flags that disable the password manager and security alerts.
        # Disable Password Check in Chrome Options
        temp_profile = os.path.join(os.getcwd(), "temp_profile_chrome")
        os.makedirs(temp_profile, exist_ok=True)

        options = Options()
        options.add_argument(f"--user-data-dir={temp_profile}")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Provide a valid browser name")

    driver.maximize_window()

    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver

    # FINALIZER to take screenshot BEFORE quitting the driver
    def teardown():
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                print("Test failed, taking screenshot...")
                screenshot_dir = os.path.join(os.getcwd(), "screenshot")
                os.makedirs(screenshot_dir, exist_ok=True)

                test_name = request.node.name
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                file_name = f"{test_name}_{timestamp}.png"
                file_path = os.path.join(screenshot_dir, file_name)

                result = driver.save_screenshot(file_path)
                print(f"Screenshot saved: {result}, path: {file_path}")

                allure.attach(driver.get_screenshot_as_png(), name=f"{test_name}_{timestamp}",
                              attachment_type=AttachmentType.PNG)
            except Exception as e:
                print(f"Error taking screenshot: {e}")
        print("[DEBUG] Quitting driver...")
        driver.quit()

    request.addfinalizer(teardown)
    yield driver
