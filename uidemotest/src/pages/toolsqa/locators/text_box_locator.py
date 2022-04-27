from selenium.webdriver.common.by import By


class TextBoxPageLocator:
    FULL_NAME_INPUT = (By.ID, 'userName')
    EMAIL_INPUT = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT_BUTTON = (By.ID, 'submit')
    SUBMITTED_DATA = (By.ID, 'output')
