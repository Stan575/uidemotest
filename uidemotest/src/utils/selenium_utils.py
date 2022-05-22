from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def is_element_visible(self, locator):
        """
        Returns True if a WebElement is present in DOM and visible at the moment of call (no waiting), or False
        :param locator: (locator_type, locator)
        :return: bool
        """
        element = self.get_element(locator)
        if element:
            return element.is_displayed()
        else:
            return False

    def get_element(self, locator):
        """
        Lookup for an element without waiting, returns a WebElement if present in DOM, or None
        Note: WebElement may not be visible or enabled
        :param locator: (locator_type, locator)
        :return: WebElement
        """
        try:
            return self.driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
            return None

    def wait_get_element(self, locator, timeout=None):
        """
        Wait for a WebElement to be visible (using standard or custom waiting time), then return the WebElement
        :param locator: (locator_type, locator)
        :param timeout: custom timeout in sec
        :return: WebElement
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait

        return wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, mark):
        """
        Get text from an element, no waiting. If element cannot be found return None
        :param mark: WebElement or locator as (locator_type, locator)
        :return: text: str or None if there is no text and no attribute 'value'
        """
        if not isinstance(mark, WebElement):
            element = self.get_element(mark)
        else:
            element = mark
        if element:
            text_from_element = element.text

            if text_from_element:
                return text_from_element
            else:
                return element.get_attribute('value')
        else:
            return None

    def wait_and_input_text(self, mark, text, timeout=None):
        """
        Wait for an element to be clickable (using standard or custom waiting time), then click the element
        :param mark: WebElement or locator as (locator_type, locator)
        :param text: text as a string
        :param timeout: custom timeout in sec
        :return: None
        """
        if not isinstance(mark, WebElement):
            element = self.wait_get_element(mark, timeout)
        else:
            element = mark

        element.click()
        element.clear()
        element.send_keys(text)

    def wait_and_click(self, mark, timeout=None):
        """
        Wait for an element to be clickable (using standard or custom waiting time), then click the element
        :param mark: WebElement or locator as (locator_type, locator)
        :param timeout: custom timeout in sec
        :return: None
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait

        wait.until(EC.element_to_be_clickable(mark)).click()
