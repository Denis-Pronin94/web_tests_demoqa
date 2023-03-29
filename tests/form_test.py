from pages.form_page import FormPage

from selenium import webdriver


class TestForm:
    """Сьют - TestForm."""

    class TestForm:
        """Тест - TestForm."""

        def test_form(self, driver: webdriver):
            """Тест - test_form."""
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person = form_page.fill_form_field()
            result = form_page.form_result()
            print(person)
            print(result)
            assert [person.first_name + ' ' + person.last_name] == [result[0]]
            assert [person.email] == [result[1]]
            assert [person.current_address] == [result[8]]
