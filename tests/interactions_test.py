from pages.interactions_page import SelectablePage, SortablePage

from selenium import webdriver


class TestInteractions:
    """Сьют - TestInteractions."""

    class TestSortable:
        """Тест - TestSortable."""

        def test_sortable(self, driver: webdriver):
            """Тест - test_sortable."""
            sortable = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable.open()
            list_before, list_after = sortable.change_list_order()
            grid_before, grid_after = sortable.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectable:
        """Тест - TestSelectable."""

        def test_selectable(self, driver: webdriver):
            """Тест - test_sortable."""
            selectable = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable.open()
            item_list = selectable.select_list_item()
            item_grid = selectable.select_grid_item()
            print(item_list)
            print(item_grid)
            assert len(item_list) > 0
            assert len(item_grid) > 0
