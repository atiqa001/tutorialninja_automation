from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = 'input-firstname'
    last_name_field_id = 'input-lastname'
    email_address_field_id = 'input-email'
    telephone_field_id = 'input-telephone'
    password_field_id = 'input-password'
    confirm_password_field_id = 'input-confirm-password'
    privacy_policy_checkbox_name = 'agree'
    continue_button_xpath = '//*[@id="content"]/div/div[2]/div/form/input'

    def enter_first_name(self, first_name):
        self.type_into_element(first_name, By.ID, self.first_name_field_id)

    def enter_last_name(self, last_name):
        self.type_into_element(last_name, By.ID, self.last_name_field_id)

    def enter_email_address(self, email_address):
        self.type_into_element(email_address, By.ID, self.email_address_field_id)

    def enter_telephone(self, telephone):
        self.type_into_element(telephone, By.ID,self.telephone_field_id)

    def enter_password(self, password):
        self.type_into_element(password, By.ID, self.password_field_id)

    def enter_confirm_password(self, confirm_password):
        self.type_into_element(confirm_password, By.ID, self.confirm_password_field_id)

    def select_privacy_policy(self):
        self.element_click(By.NAME, self.privacy_policy_checkbox_name)

    def click_on_continue_button(self):
        self.element_click(By.XPATH, self.continue_button_xpath)
