from uidemotest.src.utils.selenium_utils import SeleniumUtils
from uidemotest.src.pages.toolsqa.locators.text_box_locator import TextBoxPageLocator


class TextBoxPage(TextBoxPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/text-box'
        self.sl = SeleniumUtils(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def fill_out_full_name(self, name):
        self.sl.wait_and_input_text(self.FULL_NAME_INPUT, name)
        return self

    def fill_out_email(self, email):
        self.sl.wait_and_input_text(self.EMAIL_INPUT, email)
        return self

    def fill_out_current_address(self, text):
        self.sl.wait_and_input_text(self.CURRENT_ADDRESS, text)
        return self

    def fill_out_permanent_address(self, text):
        self.sl.wait_and_input_text(self.PERMANENT_ADDRESS, text)
        return self

    def clear_full_name_input(self):
        self.sl.get_element(self.FULL_NAME_INPUT).clear()
        return self

    def clear_email_input(self):
        self.sl.get_element(self.EMAIL_INPUT).clear()
        return self

    def clear_current_address_input(self):
        self.sl.get_element(self.CURRENT_ADDRESS).clear()
        return self

    def clear_permanent_address_input(self):
        self.sl.get_element(self.PERMANENT_ADDRESS).clear()
        return self

    def get_full_name_input_text(self):
        return self.sl.get_text(self.FULL_NAME_INPUT)

    def get_email_input_text(self):
        return self.sl.get_text(self.EMAIL_INPUT)

    def get_current_address_input_text(self):
        return self.sl.get_text(self.CURRENT_ADDRESS)

    def get_permanent_address_input_text(self):
        return self.sl.get_text(self.PERMANENT_ADDRESS)

    def click_submit_button(self):
        self.sl.wait_and_click(self.SUBMIT_BUTTON)
        return self

    def get_processed_data(self):
        return self.sl.get_text(self.SUBMITTED_DATA)
