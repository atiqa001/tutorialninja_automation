import time

import pytest

#from BaseTestt import BaseTestt
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


from BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):
    driver = None
   # @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_excel("ExcelFiles/tutorialninja.xlsx","LoginTest"))
    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel(r"C:\Users\Taufiq\PycharmProjects\SeleniumPythonHybridFramework\ExcelFiles\tutorialsninja.xlsx", "LoginTest"))
    def test_login_with_valid_user(self,email_address,password):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
       # time.sleep(4)/
        login_page.enter_email_address(email_address)
        login_page.enter_password(password)
        login_page.click_on_login_button()

       # time.sleep(3)
        account_page = AccountPage(self.driver)
        account_page.display_status_of_edit_your_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.generate_email_with_time_stamp())
        login_page.enter_password('123456')
        login_page.click_on_login_button()
        #time.sleep(3)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.warning_message_for_invalid_email_and_valid_password().__contains__(expected_message)
        # assert login_page.warning_message_for_invalid_email_and_valid_password() == expected_message
        # actual_text=login_page.warning_message_for_invalid_email_and_valid_password()
        # assert expected_message== actual_text

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address('qa@atilimited.net')
        login_page.enter_password('123456888')
        login_page.click_on_login_button()
        #time.sleep(3)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.warning_message_for_invalid_email_and_valid_password().__contains__(expected_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address('')
        login_page.enter_password('')
        login_page.click_on_login_button()
       # time.sleep(3)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.warning_message_for_invalid_email_and_valid_password().__contains__(expected_message)
