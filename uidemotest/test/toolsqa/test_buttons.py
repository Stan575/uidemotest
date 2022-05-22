import pytest
from uidemotest.src.pages.toolsqa.buttons import ButtonsPage

DOUBLE_CLICK_MSG = 'You have done a double click'
RIGHT_CLICK_MSG = 'You have done a right click'
DYNAMIC_CLICK_MSG = 'You have done a dynamic click'


@pytest.mark.usefixtures('init_driver')
class TestButtons:
    """
    Test suite for ToolsQA Elements :: buttons page
    """

    @pytest.mark.toolsqa
    @pytest.mark.smoke
    def test_double_click_me(self):
        buttons_page = ButtonsPage(self.driver).open()
        double_click_me_button = buttons_page.get_double_click_me_button()
        buttons_page.double_click(double_click_me_button)

        actual_message = buttons_page.get_message()
        assert actual_message == DOUBLE_CLICK_MSG, \
            f'Expected message: "{DOUBLE_CLICK_MSG}", actual: "{actual_message}"'

    @pytest.mark.toolsqa
    @pytest.mark.smoke
    def test_right_click_me(self):
        buttons_page = ButtonsPage(self.driver).open()
        right_click_me_button = buttons_page.get_right_click_me_button()
        buttons_page.right_click(right_click_me_button)

        actual_message = buttons_page.get_message()
        assert actual_message == RIGHT_CLICK_MSG, \
            f'Expected message: "{RIGHT_CLICK_MSG}", actual: "{actual_message}"'

    @pytest.mark.toolsqa
    @pytest.mark.smoke
    def test_click_me(self):
        buttons_page = ButtonsPage(self.driver).open()
        click_me_button = buttons_page.get_click_me_button()
        buttons_page.click(click_me_button)

        actual_message = buttons_page.get_message()
        assert actual_message == DYNAMIC_CLICK_MSG, \
            f'Expected message: "{DYNAMIC_CLICK_MSG}", actual: "{actual_message}"'

    @pytest.mark.toolsqa
    @pytest.mark.regression
    def test_click_all(self):
        buttons_page = ButtonsPage(self.driver).open()

        double_click_me_button = buttons_page.get_double_click_me_button()
        right_click_me_button = buttons_page.get_right_click_me_button()
        click_me_button = buttons_page.get_click_me_button()

        buttons_page.double_click(double_click_me_button)
        buttons_page.right_click(right_click_me_button)
        buttons_page.click(click_me_button)

        expected_message = f'{DOUBLE_CLICK_MSG}\n{RIGHT_CLICK_MSG}\n{DYNAMIC_CLICK_MSG}'
        actual_message = buttons_page.get_message()
        assert actual_message == expected_message, \
            f'Expected message: "{expected_message}", actual: "{actual_message}"'

    @pytest.mark.toolsqa
    @pytest.mark.regression
    def test_wrong_clicks_double_click_me_button(self):
        buttons_page = ButtonsPage(self.driver).open()
        double_click_me_button = buttons_page.get_double_click_me_button()

        buttons_page.click(double_click_me_button)
        actual_message = buttons_page.get_message()

        assert actual_message is None, f'Unexpected actual message: "{actual_message}" after ' \
                                       'click on "Double Click Me" button, should be no message.'

        buttons_page.right_click(double_click_me_button)
        actual_message = buttons_page.get_message()

        assert actual_message is None, f'Unexpected actual message: "{actual_message}" after ' \
                                       'right click on "Double Click Me" button, should be no message.'

    @pytest.mark.toolsqa
    @pytest.mark.regression
    def test_wrong_clicks_right_click_me_button(self):
        buttons_page = ButtonsPage(self.driver).open()
        right_click_me_button = buttons_page.get_right_click_me_button()

        buttons_page.click(right_click_me_button)
        actual_message = buttons_page.get_message()

        assert actual_message is None, f'Unexpected actual message: "{actual_message}" after ' \
                                       'click on "Right Click Me" button, should be no message.'

        buttons_page.double_click(right_click_me_button)
        actual_message = buttons_page.get_message()

        assert actual_message is None, f'Unexpected actual message: "{actual_message}" after ' \
                                       'double click on "Right Click Me" button, should be no message.'

    @pytest.mark.toolsqa
    @pytest.mark.regression
    def test_right_click_on_click_me_button(self):
        buttons_page = ButtonsPage(self.driver).open()
        click_me_button = buttons_page.get_click_me_button()

        buttons_page.right_click(click_me_button)
        actual_message = buttons_page.get_message()

        assert actual_message is None, f'Unexpected actual message: "{actual_message}" after ' \
                                       'right click on "Click Me" button, should be no message.'
