from selenium.webdriver.common.by import By


class ButtonsLocator:
    DOUBLE_CLICK_ME_BUTTON = (By.ID, 'doubleClickBtn')
    RIGHT_CLICK_ME_BUTTON = (By.ID, 'rightClickBtn')
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    DOUBLE_CLICK_MESSAGE = (By.ID, 'doubleClickMessage')
    RIGHT_CLICK_MESSAGE = (By.ID, 'rightClickMessage')
    DYNAMIC_CLICK_MESSAGE = (By.ID, 'dynamicClickMessage')
