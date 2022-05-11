from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from uidemotest.src.utils.selenium_utils import SeleniumUtils
from uidemotest.src.pages.toolsqa.locators.checkbox_locator import CheckboxPageLocator


class CheckboxPage(CheckboxPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/checkbox'
        self.su = SeleniumUtils(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def click_home_checkbox_label(self):
        self.su.wait_and_click(self.HOME_LABEL)
        return self

    def is_home_checkbox_checked(self):
        home_checkbox = self.su.wait.until(EC.presence_of_element_located(self.HOME_CHECKBOX))
        return home_checkbox.is_selected()

    def get_result_message(self):
        try:
            return self.su.get_text(self.RESULT_MSG)
        except NoSuchElementException:
            return ''
