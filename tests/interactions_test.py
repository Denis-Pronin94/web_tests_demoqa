import allure

from pages.interactions_page import (
    DraggablePage,
    DroppablePage,
    ResizablePage,
    SelectablePage,
    SortablePage,
)

from selenium import webdriver


@allure.suite('Interactions')
class TestInteractions:
    """Сьют - TestInteractions."""

    @allure.feature('Sortable Page')
    class TestSortable:
        """Тест - TestSortable."""

        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver: webdriver):
            """Тест - test_sortable."""
            sortable = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable.open()
            list_before, list_after = sortable.change_list_order()
            grid_before, grid_after = sortable.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    @allure.feature('Selectable Page')
    class TestSelectable:
        """Тест - TestSelectable."""

        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver: webdriver):
            """Тест - test_selectable."""
            selectable = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable.open()
            item_list = selectable.select_list_item()
            item_grid = selectable.select_grid_item()
            assert len(item_list) > 0
            assert len(item_grid) > 0

    @allure.feature('Resizable Page')
    class TestResizable:
        """Тест - TestResizable."""

        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver: webdriver):
            """Тест - test_resizable."""
            resizable = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable.open()
            max_box, min_box = resizable.change_size_resizable_box()
            max_resize, min_resize = resizable.change_size_resizable()
            print(max_box, min_box)
            print(max_resize, min_resize)
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert max_resize != min_resize

    @allure.feature('Droppable Page')
    class TestDroppable:
        """Тест - TestDroppable."""

        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver: webdriver):
            """Тест - test_simple_droppable."""
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            text = droppable.drop_simple()
            assert text == 'Dropped!'

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver: webdriver):
            """Тест - test_accept_droppable."""
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            not_accept, accept = droppable.drop_accept()
            assert not_accept == 'Drop here'
            assert accept == 'Dropped!'

        @allure.title('Check prevent propogation droppable')
        def test_prevent_propogation_droppable(self, driver: webdriver):
            """Тест - test_prevent_propogation_droppable."""
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = \
                droppable.drop_prevent_propogation()
            assert not_greedy == 'Dropped!'
            assert not_greedy_inner == 'Dropped!'
            assert greedy == 'Outer droppable'
            assert greedy_inner == 'Dropped!'

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver: webdriver):
            """Тест - test_revert_draggable_droppable."""
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            will_position_after_move, will_position_after_revert = \
                droppable.drop_revert_draggable('will')
            not_position_after_move, not_position_after_revert = \
                droppable.drop_revert_draggable('not_will')
            assert will_position_after_move != will_position_after_revert
            assert not_position_after_move == not_position_after_revert

    @allure.feature('Draggable Page')
    class TestDraggable:
        """Тест - TestDraggable."""

        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver: webdriver):
            """Тест - test_simple_draggable."""
            draggable = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable.open()
            before, after = draggable.simple_drag_box()
            assert before != after

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver: webdriver):
            """Тест - test_axis_restricted_draggable."""
            draggable = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable.open()
            draggable.axis_restricted_x()
            top_x, left_x = draggable.axis_restricted_x()
            top_y, left_y = draggable.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0
