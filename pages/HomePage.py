from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegistrationPage import RegistrationPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver

    search_box_field_name = 'search'
    search_button_xpath = '//*[@id="search"]/span/button'
    my_account_drop_menu_xpath = '//*[@id="top-links"]/ul/li[2]/a'
    login_option_xpath = '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a'
    registration_option_xpath = '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'


    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name, By.NAME, self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click(By.XPATH, self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click(By.XPATH, self.my_account_drop_menu_xpath)

    # def select_login_option(self):
    #     self.element_click(By.LINK_TEXT, self.login_option_link_text)
    #
    def select_login_option(self):
        self.element_click(By.XPATH, self.login_option_xpath)
        return LoginPage(self.driver)

    def select_registration_option(self):
        self.element_click(By.XPATH, self.registration_option_xpath)
        return RegistrationPage(self.driver)

    def is_at_home_page(self):
        """Check if current URL contains 'home' or matches exact home URL"""
        current_url = self.driver.current_url
        return "home" in current_url.lower() or current_url == "https://tutorialsninja.com/demo/index.php?route=common/home"

