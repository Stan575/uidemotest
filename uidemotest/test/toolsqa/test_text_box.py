import pytest
from uidemotest.src.pages.toolsqa.text_box import TextBoxPage
from faker import Faker

fake = Faker()
FULL_NAME = f'{fake.first_name()} {fake.last_name()}'
EMAIL = fake.email()
CURRENT_ADDRESS = fake.address().replace('\n', ' ')
PERMANENT_ADDRESS = fake.address().replace('\n', ' ')


@pytest.mark.usefixtures('init_driver')
class TestTextBox:
    """
    Test suite for text box functionality
    """

    @pytest.mark.toolsqa
    def test_fill_out_all_happy_path(self):
        expected_data = f'Name: {FULL_NAME}\n' \
                        f'Email: {EMAIL}\n' \
                        f'Current Address: {CURRENT_ADDRESS}\n' \
                        f'Permanent Address: {PERMANENT_ADDRESS}'

        assert TextBoxPage(self.driver) \
                   .open() \
                   .fill_out_full_name(FULL_NAME) \
                   .fill_out_email(EMAIL) \
                   .fill_out_current_address(CURRENT_ADDRESS) \
                   .fill_out_permanent_address(PERMANENT_ADDRESS) \
                   .click_submit_button() \
                   .get_processed_data() == expected_data, 'Problem with submitted fully filled out form.'

    @pytest.mark.toolsqa
    def test_fill_out_name(self):
        expected_data = f'Name: {FULL_NAME}'

        assert TextBoxPage(self.driver) \
                   .open().fill_out_full_name(FULL_NAME) \
                   .click_submit_button() \
                   .get_processed_data() == expected_data, 'Problem with submitted full name.'

    @pytest.mark.toolsqa
    def test_fill_out_email(self):
        expected_data = f'Email: {EMAIL}'

        assert TextBoxPage(self.driver) \
                   .open().fill_out_email(EMAIL) \
                   .click_submit_button() \
                   .get_processed_data() == expected_data, 'Problem with submitted email.'

    @pytest.mark.toolsqa
    def test_fill_out_current_address(self):
        expected_data = f'Current Address: {CURRENT_ADDRESS}'

        assert TextBoxPage(self.driver) \
                   .open().fill_out_current_address(CURRENT_ADDRESS) \
                   .click_submit_button() \
                   .get_processed_data() == expected_data, 'Problem with submitted current address.'

    @pytest.mark.toolsqa
    def test_fill_out_permanent_address(self):
        expected_data = f'Permanent Address: {PERMANENT_ADDRESS}'

        assert TextBoxPage(self.driver) \
                   .open().fill_out_permanent_address(PERMANENT_ADDRESS) \
                   .click_submit_button() \
                   .get_processed_data() == expected_data, 'Problem with submitted permanent address.'

    @pytest.mark.toolsqa
    def test_submit_empty_form(self):
        assert TextBoxPage(self.driver) \
                   .open() \
                   .click_submit_button() \
                   .get_processed_data() is None, 'Problem with submitted empty form.'

    @pytest.mark.toolsqa
    def test_clear_form(self):
        text_box_page = TextBoxPage(self.driver)

        assert text_box_page \
                   .open() \
                   .fill_out_full_name(FULL_NAME) \
                   .clear_full_name_input() \
                   .get_full_name_input_text() == '', "Text in 'Full Name' input field can not be edited."

        assert text_box_page \
                   .open() \
                   .fill_out_email(EMAIL) \
                   .clear_email_input() \
                   .get_email_input_text() == '', "Text in 'Email' input field can not be edited."

        assert text_box_page \
                   .open() \
                   .fill_out_current_address(CURRENT_ADDRESS) \
                   .clear_current_address_input() \
                   .get_current_address_input_text() == '', "Text in 'Current Address' input field can not be edited."

        assert text_box_page \
                   .open() \
                   .fill_out_permanent_address(PERMANENT_ADDRESS) \
                   .clear_permanent_address_input() \
                   .get_permanent_address_input_text() == '', "Text in 'Permanent Address' input field can not be edited."
