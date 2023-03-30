import random

from generator.generator import generated_color

from locators.widgests_locators import AccordianPageLocators, AutocompletePageLocators

from pages.base_page import BasePage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys


class AccordianPage(BasePage):
    """AccordianPage."""

    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num: str) -> list:
        """Возвращаем текст."""
        accordian = {
            'first':
                {'title': self.locators.SECTION_FIRST,
                 'content': self.locators.SECTION_CONTENT_FIRST},
            'second':
                {'title': self.locators.SECTION_SECOND,
                 'content': self.locators.SECTION_CONTENT_SECOND},
            'third':
                {'title': self.locators.SECTION_THIRD,
                 'content': self.locators.SECTION_CONTENT_THIRD},
        }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutocompletePage(BasePage):
    """AutoCompletePage."""

    locators = AutocompletePageLocators()

    def fill_input_multi(self) -> list:
        """Возвращаем текст цвета."""
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self) -> tuple:
        """Удаляем цвет."""
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self) -> list:
        """Проверяем цвет."""
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self) -> str:
        """Заполняем single."""
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self) -> str:
        """Проверяем single."""
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text
