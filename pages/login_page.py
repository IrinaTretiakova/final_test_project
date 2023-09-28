from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from .locators import RegistrFormLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Substring 'login' is absent"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "Registration form is not presented"
        
    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()    

        email_field = self.browser.find_element(*RegistrFormLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*RegistrFormLocators.PASSWORD_FIELD1)
        password_field.send_keys(password)

        repeat_password_field = self.browser.find_element(*RegistrFormLocators.PASSWORD_FIELD2)
        repeat_password_field.send_keys(password)

        registr_button = self.browser.find_element(*RegistrFormLocators.REGISTR_BUTTON)
        registr_button.click()