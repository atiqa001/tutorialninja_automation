from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_address_field_id = 'input-email'
    password_field_id="input-password"
    login_button_xpath='//*[@id="content"]/div/div[2]/div/form/input'
    warning_message='//*[@id="account-login"]/div[1]'

    def enter_email_address(self, email_address):
        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address)

    def enter_password(self,password):

        self.driver.find_element(By.ID,self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)

    def click_on_login_button(self):

        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def warning_message_for_invalid_email_and_valid_password(self):

        return self.driver.find_element(By.XPATH,self.warning_message).text

