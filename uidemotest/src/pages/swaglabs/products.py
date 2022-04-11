from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from uidemotest.src.pages.base_page import BasePage
from uidemotest.src.pages.swaglabs.locators.products_locator import ProductsPageLocator


class ProductsPage(BasePage, ProductsPageLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/inventory.html'

    def open(self):
        self.driver.get(self.url)
        return self

    def is_products_title_displayed(self):
        try:
            return self.get_element_no_wait(self.PAGE_TITLE).is_displayed()
        except NoSuchElementException:
            return False

    def is_burger_button_displayed(self):
        try:
            return self.get_element_no_wait(self.BURGER_BUTTON).is_displayed()
        except NoSuchElementException:
            return False

    def click_burger(self):
        self.get_element_no_wait(self.BURGER_BUTTON).click()
        return self

    def click_close_burger_menu(self):
        self.get_element_no_wait(self.BURGER_MENU_CLOSE_BUTTON).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

    def is_burger_menu_displayed(self):
        try:
            return self.get_element_no_wait(self.BURGER_MENU).is_dislplayed()
        except NoSuchElementException:
            return False
