from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_element(self, locator):
        """
        Lookup for an element without waiting
        :param locator: (locator_type, locator)
        :return: WebElement
        """
        return self.driver.find_element(locator[0], locator[1])

    def wait_get_element(self, locator, timeout=None):
        """
        Wait for an element to be visible (standard timeout)
        :param locator: (locator_type, locator)
        :param timeout: custom timeout in sec
        :return: WebElement
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait

        return wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, mark):
        """
        Get text from an element, no waiting
        :param mark: WebElement or locator as (locator_type, locator)
        :return: text: str
        """
        if not isinstance(mark, WebElement):
            element = self.get_element(mark)
        else:
            element = mark

        text_from_element = element.text

        if text_from_element:
            return text_from_element
        else:
            return element.get_attribute('value')

    def wait_and_input_text(self, mark, text, timeout=None):
        """
        Wait for an element to be clickable (standard timeout), then click the element
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
        Waiting for an element to be clickable using standard waiting time, then click the element
        :param mark: WebElement or locator as (locator_type, locator)
        :param timeout: custom timeout in sec
        :return: None
        """
        wait = WebDriverWait(self.driver, timeout) if timeout else self.wait

        wait.until(EC.element_to_be_clickable(mark)).click()