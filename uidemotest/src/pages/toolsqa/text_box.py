from uidemotest.src.utils.selenium_utils import SeleniumUtils
from uidemotest.src.pages.toolsqa.locators.text_box_locator import TextBoxPageLocator


class TextBoxPage(TextBoxPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/text-box'
        self.su = SeleniumUtils(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def fill_out_full_name(self, name):
        self.su.wait_and_input_text(self.FULL_NAME_INPUT, name)
        return self

    def fill_out_email(self, email):
        self.su.wait_and_input_text(self.EMAIL_INPUT, email)
        return self

    def fill_out_current_address(self, text):
        self.su.wait_and_input_text(self.CURRENT_ADDRESS, text)
        return self

    def fill_out_permanent_address(self, text):
        self.su.wait_and_input_text(self.PERMANENT_ADDRESS, text)
        return self

    def click_submit_button(self):
        self.su.wait_and_click(self.SUBMIT_BUTTON)
        return self

    def get_processed_data(self):
        return self.su.get_text(self.SUBMITTED_DATA)
