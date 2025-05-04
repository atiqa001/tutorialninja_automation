import time
from datetime import datetime
from selenium.webdriver.common.by import By
import pytest

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegistrationPage import RegistrationPage


@pytest.mark.usefixtures("setup")

class TestRegisteer:

    #def __init__(self):
    driver = None

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "taj"+time_stamp+"@gmail.com"

    def test_registration_with_mandatoryfield(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_registration_option()

        registration_page=RegistrationPage(self.driver)
        registration_page.enter_first_name('Md')
        registration_page.enter_last_name('QA')
        registration_page.enter_email_address('tester004@gmail.com')
        registration_page.enter_telephone('01923777612')
        registration_page.enter_password('123456')
        registration_page.enter_confirm_password('123456')
        registration_page.select_privacy_policy()
        registration_page.click_on_continue_button()

        time.sleep(3)
        account_success_page=AccountSuccessPage(self.driver)
        expected_result ="Your Account Has Been Created!"
        assert account_success_page.account_success_message().__eq__(expected_result)

        #assert self.driver.find_element(By.XPATH,'//*[@id="content"]/h1').text.__eq__(expected_result)

    def test_registration_with_all_field(self):

        self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, 'input-firstname').send_keys('Md')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('QA')
        self.driver.find_element(By.ID, 'input-email').send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID, 'input-telephone').send_keys('01923777612')

        self.driver.find_element(By.ID, 'input-password').send_keys('123456')
        self.driver.find_element(By.ID, 'input-confirm').send_keys('123456')

        self.driver.find_element(By.XPATH,'//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input').click()

        self.driver.find_element(By.NAME, 'agree').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[2]').click()
        time.sleep(3)
        expected_result = 'Your Account Has Been Created!'
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/h1').text.__eq__(expected_result)

    def test_register_with_duplicate_emai(self):

        self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, 'input-firstname').send_keys('Md')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('QA')
        self.driver.find_element(By.ID, 'input-email').send_keys('tester004@gmail.com')
        self.driver.find_element(By.ID, 'input-telephone').send_keys('01923777612')

        self.driver.find_element(By.ID, 'input-password').send_keys('123456')
        self.driver.find_element(By.ID, 'input-confirm').send_keys('123456')

        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input').click()

        self.driver.find_element(By.NAME, 'agree').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[2]').click()
        time.sleep(3)
        expected_result = 'Warning: E-Mail Address is already registered!'
        assert self.driver.find_element(By.XPATH, '//*[@id="account-register"]/div[1]').text.__eq__(expected_result)

    def test_register_without_anydata(self):

        self.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        # driver.find_element(By.ID, 'input-firstname').send_keys()
        # driver.find_element(By.ID, 'input-lastname').send_keys()
        # driver.find_element(By.ID, 'input-email').send_keys()
        # driver.find_element(By.ID, 'input-telephone').send_keys()
        #
        # driver.find_element(By.ID, 'input-password').send_keys()
        # driver.find_element(By.ID, 'input-confirm').send_keys()

        # driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input').click()
        #
        # driver.find_element(By.NAME, 'agree').click()
        # time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[2]').click()
        time.sleep(3)
        expected_result1 = 'Warning: You must agree to the Privacy Policy!'
        assert self.driver.find_element(By.XPATH, '//*[@id="account-register"]/div[1]').text.__eq__(expected_result1)

        expected_result2 = 'First Name must be between 1 and 32 characters!'
        assert self.driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div/div').text.__eq__(expected_result2)

        expected_result3 = 'Last Name must be between 1 and 32 characters!'
        assert self.driver.find_element(By.XPATH, '//*[@id="account"]/div[3]/div/div').text.__eq__(expected_result3)

        expected_result4 = 'E-Mail Address does not appear to be valid!'
        assert self.driver.find_element(By.XPATH, '//*[@id="account"]/div[4]/div/div').text.__eq__(expected_result4)

        expected_result5 = 'Telephone must be between 3 and 32 characters!'
        assert self.driver.find_element(By.XPATH, '//*[@id="account"]/div[5]/div/div').text.__eq__(expected_result5)

        expected_result6 = 'Password must be between 4 and 20 characters!'
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[2]/div[1]/div/div').text.__eq__(expected_result6)
