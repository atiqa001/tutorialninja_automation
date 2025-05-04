from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = 'search'
    search_button_xpath = '//*[@id="search"]/span/button'
    my_account_drop_menu = '//*[@id="top-links"]/ul/li[2]/a'
    login_option_link_text = 'Login'
    registration_option_link_text = 'Register'

    def enter_product_into_search_box_field(self, product_name):
        search_box=(self.driver.find_element(By.NAME, self.search_box_field_name))
        search_box.click()
        search_box.clear()
        search_box.send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def select_registration_option(self):
        self.driver.find_element(By.LINK_TEXT, self.registration_option_link_text).click()
