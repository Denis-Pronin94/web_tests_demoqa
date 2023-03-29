import random
import time

from locators.alerts_frame_windows_locators import AlertsPageLocators, BrowserWindowPageLocators

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


class AlertsPage(BasePage):
    """AlertPage."""

    locators = AlertsPageLocators()

    def check_see_alert(self) -> str:
        """Проверяем текст алерта."""
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self) -> str:
        """Проверяем аллерт после 5 секунд."""
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self) -> str:
        """Проверяем аллерт после выбора."""
        self.element_is_visible(self.locators.CONFIRM_BOX_AFTER_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        return self.element_is_present(self.locators.CONFIRM_RESULT).text

    def check_prompt_alert(self) -> tuple:
        """Проверяем аллерт после ввода."""
        text = f'autotest{random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result
