from locators.alerts_frame_windows_locators import BrowserWindowPageLocators

from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    """BrowserWindowPage."""

    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self) -> str:
        """Проверяем новую вкладку."""
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_present(self.locators.TITLE_NEW).text

    def check_opened_new_window(self) -> str:
        """Проверяем новую вкладку."""
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_present(self.locators.TITLE_NEW).text
