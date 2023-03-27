from pages.elements_page import CheckBoxPage, TextBoxPage


class TestElements:
    """Сьют - TestElements."""

    class TestTextBox:
        """Тест - text_box."""

        def test_text_box(self, driver: str):
            """Тест - text_box."""
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, 'Введенные данные и данные из таблицы не совпадают'

    class TestCheckBox:
        """Тест - check_box."""

        def test_check_box(self, driver: str):
            """Тест - check_box."""
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            input_check_box = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_check_box == output_result, 'check_box не были установлены'
