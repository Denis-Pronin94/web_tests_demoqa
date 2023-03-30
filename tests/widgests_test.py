from pages.widgests_page import (
    AccordianPage,
    AutocompletePage,
    DatePickerPage,
    ProgressBarPage,
    SliderPage,
    TabsPage,
    ToolTipsPage,
)

import pytest

from selenium import webdriver


class TestWidgets:
    """Сьют - TestWidgets."""

    class TestAccordian:
        """Тест - TestAccordian."""

        def test_accordian(self, driver: webdriver):
            """Тест - test_accordian."""
            accordian = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian.open()
            first_title, first_content = accordian.check_accordian('first')
            second_title, second_content = accordian.check_accordian('second')
            third_title, third_content = accordian.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutocomplete:
        """Тест - TestAutoComplete."""

        def test_fill_multi_autocomplete(self, driver: webdriver):
            """Тест - test_fill_multi_autocomplete."""
            autocomplete = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete.open()
            colors = autocomplete.fill_input_multi()
            colors_result = autocomplete.check_color_in_multi()
            assert colors == colors_result

        def test_remove_value_from_multi(self, driver: webdriver):
            """Тест - test_remove_value_from_multi."""
            autocomplete = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete.open()
            autocomplete.fill_input_multi()
            count_value_before, count_value_after = autocomplete.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_autocomplete(self, driver: webdriver):
            """Тест - test_fill_single_autocomplete."""
            autocomplete = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete.open()
            color = autocomplete.fill_input_single()
            color_result = autocomplete.check_color_in_single()
            assert color == color_result

    class TestDatePiker:
        """Тест - TestDatePiker."""

        def test_change_date(self, driver: webdriver):
            """Тест - test_fill_multi_autocomplete."""
            date_picker = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker.open()
            value_date_before, value_date_after = date_picker.select_date()
            assert value_date_before != value_date_after

        def test_change_date_and_time(self, driver: webdriver):
            """Тест - test_fill_multi_autocomplete."""
            date_picker = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker.open()
            value_date_before, value_date_after = date_picker.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after

    class TestSlider:
        """Тест - TestSlider."""

        def test_slider(self, driver: webdriver):
            """Тест - test_slider."""
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after

    class TestProgressBar:
        """Тест - TestProgressBar."""

        def test_progress_bar(self, driver: webdriver):
            """Тест - test_progress_bar."""
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after

    class TestTabs:
        """Тест - TestTabs."""

        @pytest.mark.skip(reason='Баг - невозможно нажать на кнопку "More"')
        def test_tabs(self, driver: webdriver):
            """Тест - test_tabs."""
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            more_button, more_content = tabs.check_tabs('more')
            assert what_button == 'What' and what_content != 0
            assert origin_button == 'Origin' and origin_content != 0
            assert use_button == 'Use' and use_content != 0
            assert more_button == 'More' and more_content != 0

    class TestToolTips:
        """Тест - TestTabs."""

        def test_tool_tips(self, driver: webdriver):
            """Тест - test_tool_tips."""
            tool_tips = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips.open()
            button_text, field_text, contrary_text, section_text = tool_tips.check_tool_tips()
            assert button_text == 'You hovered over the Button'
            assert field_text == 'You hovered over the text field'
            assert contrary_text == 'You hovered over the Contrary'
            assert section_text == 'You hovered over the 1.10.32'
