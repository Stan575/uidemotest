import pytest

from uidemotest.src.pages.toolsqa.checkbox import CheckboxPage


@pytest.mark.usefixtures('init_driver')
class TestCheckbox:

    @pytest.mark.toolsqa
    def test_home_checkbox(self):
        checkbox_page = CheckboxPage(self.driver)
        checkbox_page.open()

        # verify home checkbox is unchecked (empty)
        assert checkbox_page.is_home_checkbox_checked() is False

        # verify no result message
        assert not checkbox_page.get_result_message()

        # click home checkbox
        checkbox_page.click_home_checkbox_label()

        # verify home checkbox is checked
        assert checkbox_page.is_home_checkbox_checked()

        # verify result message text
        message_strings = [
            'home', 'desktop', 'notes', 'commands', 'documents', 'workspace', 'react',
            'angular', 'veu', 'office', 'public', 'private', 'classified', 'general', 'general', 'downloads',
            'wordFile', 'excelFile'
        ]
        actual_message = checkbox_page.get_result_message()
        missing_strings = []
        for string in message_strings:
            if string not in actual_message:
                missing_strings.append(string)

        assert  not missing_strings, f'Missing strings in result message: {missing_strings}'
