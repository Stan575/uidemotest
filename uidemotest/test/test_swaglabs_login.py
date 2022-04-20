import pytest
from uidemotest.src.pages.swaglabs.login import LoginPage
from uidemotest.src.pages.swaglabs.products import ProductsPage
import time


@pytest.mark.usefixtures('init_driver')
class TestLogin:
    """
    Test suite for login functionality
    """

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_as_standard_user(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username(login_page.get_standard_username())
        login_page.enter_password(login_page.get_password())
        start_time = time.time()
        login_page.press_login_button()

        assert ProductsPage(self.driver).is_burger_button_displayed(), 'Failed to login'
        login_time = time.time() - start_time
        assert login_time <= 4, f'Products page displayed in {login_time:.2f} sec after successful login, ' \
                                f'expected in up to 4 sec'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_as_problem_user(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username(login_page.get_problem_user_username())
        login_page.enter_password(login_page.get_password())
        start_time = time.time()
        login_page.press_login_button()

        assert ProductsPage(self.driver).is_burger_button_displayed(), 'Failed to login'
        login_time = time.time() - start_time
        assert login_time <= 4, f'Products page displayed in {login_time:.2f} sec after successful login, ' \
                                f'expected in up to 4 sec'

    @pytest.mark.skip(reason='fails because of performance issue, expected behavior')
    @pytest.mark.swaglabs
    @pytest.mark.login
    @pytest.mark.slow
    def test_login_as_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username(login_page.get_performance_glitch_username())
        login_page.enter_password(login_page.get_password())
        start_time = time.time()
        login_page.press_login_button()

        assert ProductsPage(self.driver).is_burger_button_displayed(), 'Failed to login'
        login_time = time.time() - start_time
        assert login_time <= 4, f'Products page displayed in {login_time:.2f} sec after successful login, ' \
                                f'expected in up to 4 sec'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_as_locked_out_user(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username(login_page.get_locked_out_username())
        login_page.enter_password(login_page.get_password())
        login_page.press_login_button()
        products_page = ProductsPage(self.driver)

        assert not products_page.is_burger_button_displayed(), 'Locked out user logged in'
        assert login_page.get_error_message() == 'Epic sadface: Sorry, this user has been locked out.', \
            'Problem with error message for locked out user'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username(login_page.get_standard_username())
        login_page.enter_password(login_page.get_password()[:-1])
        login_page.press_login_button()
        products_page = ProductsPage(self.driver)

        assert not products_page.is_burger_button_displayed(), 'Logged in with invalid password'
        assert login_page.get_error_message() == \
               'Epic sadface: Username and password do not match any user in this service', \
                'Problem with error message for username and password match'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_invalid_username(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username('standard user')
        login_page.enter_password(login_page.get_password())
        login_page.press_login_button()
        products_page = ProductsPage(self.driver)

        assert not products_page.is_burger_button_displayed(), 'Logged in with invalid username'
        assert login_page.get_error_message() == \
               'Epic sadface: Username and password do not match any user in this service', \
                'Problem with error message for username and password match'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_missing_password(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_username(login_page.get_standard_username())
        login_page.press_login_button()
        products_page = ProductsPage(self.driver)

        assert not products_page.is_burger_button_displayed(), 'Logged in with missing password'
        assert login_page.get_error_message() == 'Epic sadface: Password is required', \
            'Problem with error message for missing password'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_missing_username(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_password(login_page.get_password())
        login_page.press_login_button()
        products_page = ProductsPage(self.driver)

        assert not products_page.is_burger_button_displayed(), 'Logged in with missing username'
        assert login_page.get_error_message() == 'Epic sadface: Username is required', \
            'Problem with error message for missing username'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_missing_username_password(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.press_login_button()
        products_page = ProductsPage(self.driver)

        assert not products_page.is_burger_button_displayed(), 'Logged in with missing username & password'
        assert login_page.get_error_message() == 'Epic sadface: Username is required', \
            'Problem with error message for missing username'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_login_password_mask(self):
        password_input_field_type_value = LoginPage(self.driver).open().get_password_input_field_type_value()

        assert password_input_field_type_value == 'password', 'Password input field "type" value is not "password"'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_logout(self):
        self.test_login_as_standard_user()
        products_page = ProductsPage(self.driver)
        products_page.click_burger()
        products_page.click_logout()

        assert not products_page.is_burger_menu_displayed(), 'Failed to logout'
        assert not products_page.is_burger_button_displayed(), 'Failed to logout'
        assert not products_page.is_products_title_displayed(), 'Failed to logout'
        assert LoginPage(self.driver).is_login_page_displayed(), 'Login page is not displayed after logout'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_logout_back(self):
        self.test_logout()
        self.driver.back()
        login_page = LoginPage(self.driver)

        assert login_page.is_login_page_displayed(), 'Logged in by navigating back after logout'
        assert login_page.get_error_message() == \
               "Epic sadface: You can only access '/inventory.html' when you are logged in.", \
               'Problem with access error message'

    @pytest.mark.swaglabs
    @pytest.mark.login
    def test_direct_access_attempt(self):
        ProductsPage(self.driver).open()
        login_page = LoginPage(self.driver)

        assert login_page.is_login_page_displayed(), 'No redirection to login page'
        assert login_page.get_error_message() == \
               "Epic sadface: You can only access '/inventory.html' when you are logged in.", \
               'Problem with access error message'
