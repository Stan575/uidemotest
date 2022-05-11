from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from uidemotest.src.pages.toolsqa.locators.rado_button_locator import RadioButtonLocator
from uidemotest.src.utils.selenium_utils import SeleniumUtils


class RadioButtonPage(RadioButtonLocator):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/radio-button'
        self.sl = SeleniumUtils(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def get_page_header(self):
        return self.sl.get_text(self.sl.wait_get_element(self.PAGE_MAIN_HEADER))

    def get_question_text(self):
        return self.sl.get_text(self.QUESTION_TEXT)

    def is_radio_button_enabled(self, name):
        return self.sl.get_element((By.ID, f'{name.lower()}Radio')).is_enabled()

    def is_radio_button_checked(self, name):
        return self.sl.get_element((By.ID, f'{name.lower()}Radio')).is_selected()

    def click_radio_button(self, name):
        self.sl.get_element((By.CSS_SELECTOR, f'label[for={name.lower()}Radio]')).click()
        return self

    def get_message_text(self):
        try:
            return self.sl.get_text(self.RESULT_ENTIRE_MESSAGE)
        except NoSuchElementException:
            return ''

    def get_message_text_color(self):
        text_element = self.sl.get_element(self.RESULT_MESSAGE)
        rgb_color = text_element.value_of_css_property('color')
        return rgb_color
