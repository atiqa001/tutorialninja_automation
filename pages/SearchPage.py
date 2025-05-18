from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_xpath = '//*[@id="content"]/div[3]/div/div/div[2]/div[1]/h4/a'

    no_product_message_xpath = '//*[@id="content"]/p[2]'

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element(By.XPATH, self.valid_hp_product_xpath)

    def retrieve_no_product_message(self):
        return self.retrieve_text_from_element(By.XPATH, self.no_product_message_xpath)

