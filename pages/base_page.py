from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    """Базовый Page."""

    def __init__(self, driver: webdriver, url: str):
        """Базовый driver и url."""
        self.driver = driver
        self.url = url

    def open(self):
        """Открыть браузер."""
        self.driver.get(self.url)

    def element_is_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Видимый элемент."""
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Видимые элементы."""
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не обязательно видимый элемент."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не обязательно видимые элементы."""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не видимый элемент."""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator: str, timeout: int = 5) -> wait.mro():
        """Не видимые элементы."""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element: str):
        """Переместиться к элементы."""
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def action_double_click(self, element: str):
        """Двойной клик."""
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element: str):
        """Клик правой кнопкой мыши."""
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element: str, x_coords: int, y_coords: int):
        """Двигаем оп координатам."""
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_move_to_element(self, element: str):
        """Двигаем оп координатам."""
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def remove_footer(self):
        """Удаляем футер."""
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
