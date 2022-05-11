import pytest
from uidemotest.src.pages.toolsqa.radio_button import RadioButtonPage

PAGE_HEADER = 'Radio Button'
QUESTION = 'Do you like the site?'
MESSAGE_BASE_TEXT = 'You have selected '
YES = 'Yes'
IMPRESSIVE = 'Impressive'
NO = 'No'
COLOR = 'rgba(40, 167, 69, 1)'  # hex: #28a745 (dark green)


@pytest.mark.usefixtures('init_driver')
class TestRadioButton:
    """
    Test suite for radio-buttons
    """

    @pytest.mark.toolsqa
    @pytest.mark.regression
    def test_page_default_state(self):
        radio_button_page = RadioButtonPage(self.driver).open()

        # verify page header
        actual_page_header = radio_button_page.get_page_header()
        assert actual_page_header == PAGE_HEADER, \
            f"Wrong page header: '{actual_page_header}', expected: '{PAGE_HEADER}'."

        # verify question text
        actual_question = radio_button_page.get_question_text()
        assert actual_question == QUESTION, f"Wrong question text: '{actual_question}', expected: '{QUESTION}'."

        # verify all radio buttons are unchecked, 'Yes' and 'Impressive' are enabled, 'No' is disabled
        assert radio_button_page.is_radio_button_checked(YES) is False, \
            f"'{YES}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(YES) is True, \
            f"'{YES}' radio button is disabled by default, must be enabled."

        assert radio_button_page.is_radio_button_checked(IMPRESSIVE) is False, \
            f"'{IMPRESSIVE}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(IMPRESSIVE) is True, \
            f"'{IMPRESSIVE}' radio button is disabled by default, must be enabled."

        assert radio_button_page.is_radio_button_checked(NO) is False, \
            f"'{NO}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(NO) is False, \
            f"'{NO}' radio button is enabled, must be disabled."

        # verify no message
        actual_message = radio_button_page.get_message_text()
        assert actual_message == '', f"Actual message: '{actual_message}', expected no message."

    @pytest.mark.toolsqa
    @pytest.mark.smoke
    def test_yes_radio_button(self):
        # click 'Yes' radio button
        radio_button_page = RadioButtonPage(self.driver) \
            .open() \
            .click_radio_button(YES)

        # verify Yes button is checked
        assert radio_button_page.is_radio_button_checked(YES) is True, \
            f"'{YES}' radio button is unchecked after click."

        # verify 'Yes' message
        actual_message = radio_button_page.get_message_text()
        expected_message = MESSAGE_BASE_TEXT + YES
        assert actual_message == expected_message, \
            f"Actual message: '{actual_message}', expected message: '{expected_message}'."

        # verify message text color
        actual_message_text_color = radio_button_page.get_message_text_color()
        assert actual_message_text_color == COLOR, \
            f"Unexpected '{YES}' message text color: '{actual_message_text_color}', expected: '{COLOR}'."

        assert radio_button_page.is_radio_button_checked(IMPRESSIVE) is False, \
            f"'{IMPRESSIVE}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(IMPRESSIVE) is True, \
            f"'{IMPRESSIVE}' radio button is disabled by default, must be enabled."

        assert radio_button_page.is_radio_button_checked(NO) is False, \
            f"'{NO}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(NO) is False, \
            f"'{NO}' radio button is enabled, must be disabled."

    @pytest.mark.toolsqa
    @pytest.mark.smoke
    def test_impressive_radio_button(self):
        # click 'Impressive' radio button
        radio_button_page = RadioButtonPage(self.driver) \
            .open() \
            .click_radio_button(IMPRESSIVE)

        # verify Impressive button is checked
        assert radio_button_page.is_radio_button_checked(IMPRESSIVE) is True, \
            f"'{IMPRESSIVE}' radio button is unchecked after click."

        # verify 'Impressive' message
        actual_message = radio_button_page.get_message_text()
        expected_message = MESSAGE_BASE_TEXT + IMPRESSIVE
        assert actual_message == expected_message, \
            f"Actual message: '{actual_message}', expected message: '{expected_message}'."

        # verify message text color
        actual_message_text_color = radio_button_page.get_message_text_color()
        assert actual_message_text_color == COLOR, \
            f"Unexpected '{IMPRESSIVE}' message text color: '{actual_message_text_color}', expected: '{COLOR}'."

        assert radio_button_page.is_radio_button_checked(YES) is False, \
            f"'{YES}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(YES) is True, \
            f"'{YES}' radio button is disabled by default, must be enabled."

        assert radio_button_page.is_radio_button_checked(NO) is False, \
            f"'{NO}' radio button is checked by default, must be unchecked."
        assert radio_button_page.is_radio_button_enabled(NO) is False, \
            f"'{NO}' radio button is enabled, must be disabled."

    @pytest.mark.toolsqa
    @pytest.mark.regression
    def test_change_selection(self):
        # click 'Yes' radio button, then 'Impressive' radio button
        radio_button_page = RadioButtonPage(self.driver) \
            .open() \
            .click_radio_button(YES) \
            .click_radio_button(IMPRESSIVE)

        # verify 'Impressive' message
        actual_message = radio_button_page.get_message_text()
        expected_message = MESSAGE_BASE_TEXT + IMPRESSIVE
        assert actual_message == expected_message, \
            f"Actual message: '{actual_message}', expected message: '{expected_message}'."

        # click 'Yes' radio button
        radio_button_page.click_radio_button(YES)

        # verify 'Yes' message
        actual_message = radio_button_page.get_message_text()
        expected_message = MESSAGE_BASE_TEXT + YES
        assert actual_message == expected_message, \
            f"Actual message: '{actual_message}', expected message: '{expected_message}'."
