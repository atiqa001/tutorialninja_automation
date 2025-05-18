from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_success_xpath='//*[@id="content"]/h1'

    def account_success_message(self):
        return self.retrieve_text_from_element('account_success_xpath',self.account_success_xpath)
