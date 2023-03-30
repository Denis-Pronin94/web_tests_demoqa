from pages.interactions_page import SortablePage

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
