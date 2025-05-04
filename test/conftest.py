import pytest
from selenium import webdriver
from utilities import ReadConfigurations


@pytest.fixture
def setup(request):
    # Read browser and URL configurations
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    if not browser:
        raise ValueError("Browser configuration is missing")

    # Browser setup
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError('Provide a Valid Browser Name')

    # Maximize a window
    driver.maximize_window()

    # Load application URL
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    if not app_url:
        raise ValueError("Application URL is missing in configurations")

    driver.get(app_url)

    # Assign a driver to the test class (if required)
    request.cls.driver = driver

    # Cleanup after a test
    yield driver
    if driver:
        driver.quit()
