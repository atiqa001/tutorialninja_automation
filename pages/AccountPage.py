from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_information_xpath = '//*[@id="content"]/ul[1]/li[1]/a'

    def display_status_of_edit_your_account_information(self):
        return self.check_display_status_of_element(By.XPATH,self.edit_your_account_information_xpath)

