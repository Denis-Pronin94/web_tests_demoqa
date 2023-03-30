from pages.interactions_page import ResizablePage, SelectablePage, SortablePage

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
            """Тест - test_selectable."""
            selectable = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable.open()
            item_list = selectable.select_list_item()
            item_grid = selectable.select_grid_item()
            assert len(item_list) > 0
            assert len(item_grid) > 0

    class TestResizable:
        """Тест - TestSelectable."""

        def test_resizable(self, driver: webdriver):
            """Тест - test_sortable."""
            resizable = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable.open()
            max_box, min_box = resizable.change_size_resizable_box()
            max_resize, min_resize = resizable.change_size_resizable()
            print(max_box, min_box)
            print(max_resize, min_resize)
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert max_resize != min_resize
