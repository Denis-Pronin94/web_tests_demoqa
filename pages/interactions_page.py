import random

from locators.interactions_locators import (
    ResizablePageLocators,
    SelectablePageLocators,
    SortablePageLocators,
)

from pages.base_page import BasePage


class SortablePage(BasePage):
    """SortablePage."""

    locators = SortablePageLocators()

    def get_sortable_item(self, elements: str) -> list:
        """Возвращаем массив."""
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self) -> tuple:
        """Возвращаем массив после drag_and_drop."""
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_item(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self) -> tuple:
        """Возвращаем массив после drag_and_drop."""
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    """SelectablePage."""

    locators = SelectablePageLocators()

    def click_selectable_item(self, element: str):
        """Возвращаем массив после drag_and_drop."""
        item_list = self.elements_are_visible(element)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self) -> str:
        """Возвращаем текст елемента."""
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self) -> str:
        """Возвращаем текст елемента."""
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    """ResizablePage."""

    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size: str) -> tuple:
        """Возвращаем размер окна."""
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element: str) -> str:
        """Возвращаем размер окна."""
        size = self.element_is_present(element)
        return size.get_attribute('style')

    def change_size_resizable_box(self) -> tuple:
        """Возвращаем максимальный и минимальный размер окна."""
        self.action_drag_and_drop_by_offset(
            self.element_is_present(
                self.locators.RESIZABLE_BOX_HANDLE), 300, 150)
        max_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(
            self.element_is_present(
                self.locators.RESIZABLE_BOX_HANDLE), -600, -400)
        min_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self) -> tuple:
        """Возвращаем максимальный и минимальный размер окна."""
        self.action_drag_and_drop_by_offset(
            self.element_is_visible(
                self.locators.RESIZABLE_HANDLE),
            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(
            self.get_max_min_size(
                self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(
            self.element_is_visible(
                self.locators.RESIZABLE_HANDLE),
            random.randint(-200, -1), random.randint(-200, -1))
        mix_size = self.get_px_from_width_height(
            self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, mix_size
