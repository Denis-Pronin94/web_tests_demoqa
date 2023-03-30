import random
import time

from generator.generator import generated_color, generated_date

from locators.widgests_locators import (
    AccordianPageLocators,
    AutocompletePageLocators,
    DatePickerPageLocators,
    ProgressBarPageLocators,
    SliderPageLocators,
)

from pages.base_page import BasePage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


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


class DatePickerPage(BasePage):
    """AutoCompletePage."""

    locators = DatePickerPageLocators()

    def select_date(self) -> tuple:
        """Проверяем single."""
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self) -> tuple:
        """Выбираем text."""
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2023')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element: str, value: str):
        """Выбираем text."""
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, element: str, value: str):
        """Проверяем text."""
        item_list = self.elements_are_present(element)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    """SliderPage."""

    locators = SliderPageLocators()

    def change_slider_value(self) -> tuple:
        """Возвращаем значение слайдера."""
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    """ProgressBarPage."""

    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self) -> tuple:
        """Возвращаем текст progress_bar."""
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after