from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def get_element_no_wait(self, locator):
        """
        Looking for an element without waiting
        :param locator: (By strategy, locator)
        :return: WebElement
        """
        return self.driver.find_element(locator[0], locator[1])

    def get_element(self, locator):
        """
        Waiting for an element to be visible using standard waiting time
        :param locator: (By strategy, locator)
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, mark):
        """
        Method returns text from an element
        :param mark: WebElement or locator
        :return: text: str
        """
        if not isinstance(mark, WebElement):
            element = self.get_element_no_wait(mark)
        else:
            element = mark

        if element.text:
            return element.text
        else:
            return element.get_attribute('value')
