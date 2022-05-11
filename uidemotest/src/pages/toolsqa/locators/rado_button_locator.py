from selenium.webdriver.common.by import By


class RadioButtonLocator:
    PAGE_MAIN_HEADER = (By.CLASS_NAME, 'main-header')
    QUESTION_TEXT = (By.CLASS_NAME, 'mb-3')

    RESULT_MESSAGE = (By.CSS_SELECTOR, 'span.text-success')
    RESULT_ENTIRE_MESSAGE = (By.CSS_SELECTOR, 'p.mt-3')
