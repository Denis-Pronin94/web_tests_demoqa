import random
from http import HTTPStatus

import allure

from pages.elements_page import (
    ButtonsPage,
    CheckBoxPage,
    DynamicPropertiesPage,
    LinksPage,
    RadioButtonPage,
    TextBoxPage,
    UploadAndDownloadPage,
    WebTablePage,
)

import pytest

from selenium import webdriver


@allure.suite('Elements')
class TestElements:
    """Сьют - TestElements."""

    @allure.feature('TextBox')
    class TestTextBox:
        """Тест - TestTextBox."""

        @allure.title('Check TextBox')
        def test_text_box(self, driver: webdriver):
            """Тест - text_box."""
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, 'Введенные данные и данные из таблицы не совпадают'

    @allure.feature('CheckBox')
    class TestCheckBox:
        """Тест - TestCheckBox."""

        @allure.title('Check CheckBox')
        def test_check_box(self, driver: webdriver):
            """Тест - check_box."""
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_check_box = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_check_box == output_result, 'check_box не были установлены'

    @allure.feature('RadioButton')
    class TestRadioButton:
        """Тест - TestRadioButton."""

        @allure.title('Check RadioButton')
        @pytest.mark.skip(reason='Баг - радиокнопка "No" не кликается')
        def test_radio_button(self, driver: webdriver):
            """Тест -test_radio_button."""
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            assert output_no == 'No'

    @allure.feature('WebTable')
    class TestWebTable:
        """Тест - TestWebTable."""

        @allure.title('Сheck to add a person to the table')
        def test_web_table_and_person(self, driver: webdriver):
            """Тест - test_web_table_and_person."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver: webdriver):
            """Тест - test_web_table_search_person."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result

        @allure.title('Checking to update the persons info in the table')
        def test_web_table_update_person_info(self, driver: webdriver):
            """Тест - test_web_table_update_person_info."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row

        @allure.title('Checking to remove a person from the table')
        def test_web_table_delete_person(self, driver: webdriver):
            """Тест - test_web_table_update_person_info."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @allure.title('Check the change in the number of rows in the table')
        @pytest.mark.skip(reason='Баг - не возможно открыть боллее 25 строк')
        def test_table_change_count_row(self, driver: webdriver):
            """Тест - test_table_change_count_row."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100]

    @allure.feature('Buttons page')
    class TestButton:
        """Тест - TestButton."""

        @allure.title('Checking clicks of different types')
        def test_different_click_on_the_buttons(self, driver: webdriver):
            """Тест - test_different_click_on_the_buttons."""
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'

    @allure.feature('Links page')
    class TestLinks:
        """Тест - TestButton."""

        @allure.title('Checking the link')
        def test_check_link(self, driver: webdriver):
            """Тест - test_check_link."""
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url

        @allure.title('Checking the broken link')
        def test_broken_link(self, driver: webdriver):
            """Тест - test_broken_link."""
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == HTTPStatus.BAD_REQUEST

    @allure.feature('Upload and Download page')
    class TestUploadAndDownload:
        """Тест - TestDownload."""

        @allure.title('Check upload file')
        def test_upload_file(self, driver: webdriver):
            """Тест - test_upload_file."""
            upload_download_page = UploadAndDownloadPage(
                driver,
                'https://demoqa.com/upload-download',
            )
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result

        @allure.title('Check download file')
        def test_download_file(self, driver: webdriver):
            """Тест - test_download_file."""
            upload_download_page = UploadAndDownloadPage(
                driver,
                'https://demoqa.com/upload-download',
            )
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True

    @allure.feature('Dynamic properties page')
    class TestDynamicProperties:
        """Тест - TestDynamicProperties."""

        @allure.title('Check dynamic properties')
        def test_dynamic_properties(self, driver: webdriver):
            """Тест - test_dynamic_properties."""
            dynamic_properties_page = DynamicPropertiesPage(
                driver,
                'https://demoqa.com/dynamic-properties',
            )
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            dynamic_properties_page.check_appear_button()
            assert color_after != color_before

        @allure.title('Check appear button')
        def test_appear_button(self, driver: webdriver):
            """Тест - test_appear_button."""
            dynamic_properties_page = DynamicPropertiesPage(
                driver,
                'https://demoqa.com/dynamic-properties',
            )
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True

        @allure.title('Check enable button')
        def test_enable_button(self, driver: webdriver):
            """Тест - test_appear_button."""
            dynamic_properties_page = DynamicPropertiesPage(
                driver,
                'https://demoqa.com/dynamic-properties',
            )
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True
