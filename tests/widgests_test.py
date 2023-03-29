

from selenium import webdriver

from pages.widgests_page import AccordianPage


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



