from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_field_id = 'input-firstname'
    last_name_field_id = 'input-lastname'
    email_address_field_id = 'input-email'
    telephone_field_id = 'input-telephone'
    password_field_id = 'input-password'
    confirm_password_field_id = 'input-confirm-password'
    privacy_policy_checkbox_name = 'agree'
    continue_button_xpath = '//*[@id="content"]/div/div[2]/div/form/input'

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_field_id).click()
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name)

    def enter_email_address(self, email_address):
        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address)

    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephone_field_id).click()
        self.driver.find_element(By.ID, self.telephone_field_id).clear()
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password)

    def select_privacy_policy(self):
        self.driver.find_element(By.NAME, self.privacy_policy_checkbox_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
