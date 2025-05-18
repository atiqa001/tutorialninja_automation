from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = 'input-email'
    password_field_id = "input-password"
    login_button_xpath = '//*[@id="content"]/div/div[2]/div/form/input'
    warning_message_xpath = '//*[@id="account-login"]/div[1]'

    def enter_email_address(self, email_address):
        self.type_into_element(email_address, By.ID, self.email_address_field_id)

    def enter_password(self, password):
        self.type_into_element(password, By.ID, self.password_field_id)

    def click_on_login_button(self):
        self.element_click(By.XPATH, self.login_button_xpath)

    def warning_message_for_invalid_email_and_valid_password(self):
        return self.retrieve_text_from_element(By.XPATH, self.warning_message_xpath)
