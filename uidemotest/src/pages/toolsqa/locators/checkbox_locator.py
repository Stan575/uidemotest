from selenium.webdriver.common.by import By


class CheckboxPageLocator:

    HOME_CHECKBOX = (By.ID, 'tree-node-home')
    HOME_LABEL = (By.CSS_SELECTOR, 'label[for=tree-node-home] span.rct-title')

    RESULT_MSG = (By.ID, 'result')
