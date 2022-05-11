from selenium.webdriver.common.by import By


class LoginPageLocator:
    USER_NAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test=error]')
    ACCEPTED_USERNAMES = (By.ID, 'login_credentials')
    PASSWORD = (By.CLASS_NAME, 'login_password')
