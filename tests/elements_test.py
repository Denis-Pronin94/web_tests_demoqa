import random

from pages.elements_page import (
    CheckBoxPage,
    RadioButtonPage,
    TextBoxPage,
    WebTablePage,
)

import pytest

from selenium import webdriver


class TestElements:
    """Сьют - TestElements."""

    class TestTextBox:
        """Тест - TestTextBox."""

        def test_text_box(self, driver: webdriver):
            """Тест - text_box."""
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, 'Введенные данные и данные из таблицы не совпадают'

    class TestCheckBox:
        """Тест - TestCheckBox."""

        def test_check_box(self, driver: webdriver):
            """Тест - check_box."""
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_check_box = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_check_box == output_result, 'check_box не были установлены'

    class TestRadioButton:
        """Тест - TestRadioButton."""

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

    class TestWebTable:
        """Тест - TestWebTable."""

        def test_web_table_and_person(self, driver: webdriver):
            """Тест - test_web_table_and_person."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver: webdriver):
            """Тест - test_web_table_search_person."""
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result
