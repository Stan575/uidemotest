from uidemotest.src.pages.base_page import BasePage
from uidemotest.src.pages.swaglabs.locators.login_locator import LoginPageLocator


class LoginPage(BasePage, LoginPageLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/'

    def open(self):
        self.driver.get(self.url)
        return self

    def is_login_page_displayed(self):
        username_field_displayed = self.get_element(self.USER_NAME_FIELD)
        password_field_displayed = self.get_element_no_wait(self.PASSWORD_FIELD).is_displayed()
        login_button_displayed = self.get_element_no_wait(self.LOGIN_BUTTON).is_displayed()

        return username_field_displayed and password_field_displayed and login_button_displayed

    def enter_username(self, username):
        username_input_field = self.get_element_no_wait(self.USER_NAME_FIELD)
        username_input_field.click()
        username_input_field.send_keys(username)
        return self

    def enter_password(self, password):
        password_input_field = self.get_element_no_wait(self.PASSWORD_FIELD)
        password_input_field.click()
        password_input_field.send_keys(password)
        return self

    def press_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    def __get_accepted_usernames(self):
        usernames_text = self.get_text(self.ACCEPTED_USERNAMES)
        usernames = [string for string in usernames_text.split('\n') if string.endswith('user')]

        return usernames

    def get_standard_username(self):
        return self.__get_accepted_usernames()[0]

    def get_locked_out_username(self):
        return self.__get_accepted_usernames()[1]

    def get_problem_user_username(self):
        return self.__get_accepted_usernames()[2]

    def get_performance_glitch_username(self):
        return self.__get_accepted_usernames()[3]

    def get_password(self):
        text = self.get_text(self.PASSWORD)
        password = text.split('\n')[1]

        return password

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_password_input_field_type_value(self):
        password_input_field = self.get_element_no_wait(self.PASSWORD_FIELD)

        return password_input_field.get_attribute('type')
