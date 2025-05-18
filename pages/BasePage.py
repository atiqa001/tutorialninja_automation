
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def type_into_element(self, text, by, locator_value):
        element = self.get_element(by, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, by, locator_value):
        element = self.get_element(by, locator_value)
        element.click()

    def check_display_status_of_element(self, by, locator_value):
        element = self.get_element(by, locator_value)
        return element.is_displayed()

    def retrieve_text_from_element(self, by, locator_value):
        element = self.get_element(by, locator_value)
        return element.text

    def get_element(self, by, locator_value, timeout=20):
        locator_map = {
            "id": By.ID,
            "xpath": By.XPATH,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
            "tag_name": By.TAG_NAME,
            "class_name": By.CLASS_NAME,
            "css_selector": By.CSS_SELECTOR
        }

        selenium_by = locator_map.get(by)
        if selenium_by is None:
            raise ValueError(f"Unsupported locator type: {by}")

        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((selenium_by, locator_value)))
        except TimeoutException:
            raise TimeoutException(f"Element not found within {timeout} seconds: {by}='{locator_value}'")
        except WebDriverException as e:
            raise WebDriverException(f"Error finding element {by}='{locator_value}': {str(e)}")


