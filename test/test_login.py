import time

from BaseTestt import BaseTestt
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


# from test.BaseTest import BaseTest


class TestLogin(BaseTestt):
    driver = None

    def test_login_with_valid_user(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        time.sleep(4)
        login_page.enter_email_address('qa@atilimited.net')
        login_page.enter_password('123456')
        login_page.click_on_login_button()

        time.sleep(3)
        account_page = AccountPage(self.driver)
        account_page.display_status_of_edit_your_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.test_generate_email_with_time_stamp())
        login_page.enter_password('123456')
        login_page.click_on_login_button()
        time.sleep(3)
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
        time.sleep(3)
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
        time.sleep(3)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.warning_message_for_invalid_email_and_valid_password().__contains__(expected_message)
