from uidemotest.src.pages.toolsqa.locators.buttons_locator import ButtonsLocator
from uidemotest.src.utils.selenium_utils import SeleniumUtils
from selenium.webdriver.common.action_chains import ActionChains


class ButtonsPage(ButtonsLocator):

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/buttons'
        self.sl = SeleniumUtils(self.driver)
        self.actions = ActionChains(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def get_click_me_button(self):
        return self.sl.get_element(self.CLICK_ME_BUTTON)

    def get_double_click_me_button(self):
        return self.sl.get_element(self.DOUBLE_CLICK_ME_BUTTON)

    def get_right_click_me_button(self):
        return self.sl.get_element(self.RIGHT_CLICK_ME_BUTTON)

    def click(self, element):
        element.click()
        return self

    def double_click(self, element):
        self.actions.double_click(element).perform()
        return self

    def right_click(self, element):
        self.actions.context_click(element).perform()
        return self

    def get_message(self):
        message = None

        double_click_msg = self.sl.get_text(self.DOUBLE_CLICK_MESSAGE)
        right_click_msg = self.sl.get_text(self.RIGHT_CLICK_MESSAGE)
        dynamic_click_msg = self.sl.get_text(self.DYNAMIC_CLICK_MESSAGE)

        if double_click_msg:
            message = double_click_msg

        if message and right_click_msg:
            message += '\n' + right_click_msg
        elif right_click_msg:
            message = right_click_msg

        if message and dynamic_click_msg:
            message += '\n' + dynamic_click_msg
        elif dynamic_click_msg:
            message = dynamic_click_msg

        return message
