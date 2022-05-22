from uidemotest.src.utils.selenium_utils import SeleniumUtils
from uidemotest.src.pages.swaglabs.locators.products_locator import ProductsPageLocator


class ProductsPage(ProductsPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.saucedemo.com/inventory.html'
        self.sl = SeleniumUtils(self.driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def is_products_title_displayed(self):
        page_title = self.sl.get_element(self.PAGE_TITLE)
        if page_title:
            return page_title.is_displayed()
        else:
            return False

    def is_burger_button_displayed(self):
        burger_button = self.sl.get_element(self.BURGER_BUTTON)
        if burger_button:
            return burger_button.is_displayed()
        else:
            return False

    def click_burger(self):
        self.sl.get_element(self.BURGER_BUTTON).click()
        return self

    def click_close_burger_menu(self):
        self.sl.get_element(self.BURGER_MENU_CLOSE_BUTTON).click()

    def click_logout(self):
        self.sl.wait_and_click(self.LOGOUT_BUTTON)

    def is_burger_menu_displayed(self):
        burger_menu = self.sl.get_element(self.BURGER_MENU)
        if burger_menu:
            return burger_menu.is_displayed()
        else:
            return False
