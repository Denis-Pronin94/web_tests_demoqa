from pages.widgests_page import AccordianPage, AutocompletePage, DatePickerPage

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
