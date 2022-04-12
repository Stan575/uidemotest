from uidemotest.src.utils.selenium_utils import SeleniumUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from uidemotest.src.pages.swaglabs.locators.products_locator import ProductsPageLocator


class ProductsPage(ProductsPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.saucedemo.com/inventory.html'
        self.su = SeleniumUtils(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def is_products_title_displayed(self):
        try:
            return self.su.get_element(self.PAGE_TITLE).is_displayed()
        except NoSuchElementException:
            return False

    def is_burger_button_displayed(self):
        try:
            return self.su.get_element(self.BURGER_BUTTON).is_displayed()
        except NoSuchElementException:
            return False

    def click_burger(self):
        self.su.get_element(self.BURGER_BUTTON).click()
        return self

    def click_close_burger_menu(self):
        self.su.get_element(self.BURGER_MENU_CLOSE_BUTTON).click()

    def click_logout(self):
        self.su.wait_and_click(self.LOGOUT_BUTTON)

    def is_burger_menu_displayed(self):
        try:
            return self.su.get_element(self.BURGER_MENU).is_dislplayed()
        except NoSuchElementException:
            return False
