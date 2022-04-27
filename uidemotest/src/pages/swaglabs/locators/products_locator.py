from selenium.webdriver.common.by import By


class ProductsPageLocator:
    PAGE_TITLE = (By.CLASS_NAME, 'title')
    BURGER_BUTTON = (By.ID, 'react-burger-menu-btn')
    BURGER_MENU = (By.CSS_SELECTOR, 'bm-menu')
    BURGER_MENU_CLOSE_BUTTON = (By.ID, 'react-burger-cross-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
