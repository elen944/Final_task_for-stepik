from .base_page import BasePage
from .locators import LoginPageLocators
import time
from faker import Faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form was not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form was not presented"

    def should_be_login_url(self):
        current_url = self.browser.current_url
        login = "login"
        assert login in current_url, \
            f"Current URL is not consider '{login}' in current_url: '{current_url}'"

    def register_new_user(self):
        f = Faker()
        email = f.email()
        password = f.password()
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FIRST_PASSWORD_FIELD).send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_SECOND_PASSWORD_FIELD).send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()