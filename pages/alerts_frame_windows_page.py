import random
import time

import allure

from locators.alerts_frame_windows_locators import (
    AlertsPageLocators,
    BrowserWindowPageLocators,
    FramesPageLocators,
    ModalDialogPageLocators,
    NestedFramesLocators,
)

from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    """BrowserWindowPage."""

    locators = BrowserWindowPageLocators()

    @allure.step('check opened new tab ')
    def check_opened_new_tab(self) -> str:
        """Проверяем новую вкладку."""
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_present(self.locators.TITLE_NEW).text

    @allure.step('check opened new window')
    def check_opened_new_window(self) -> str:
        """Проверяем новую вкладку."""
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.element_is_present(self.locators.TITLE_NEW).text


class AlertsPage(BasePage):
    """AlertPage."""

    locators = AlertsPageLocators()

    @allure.step('get text from alert')
    def check_see_alert(self) -> str:
        """Проверяем текст алерта."""
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def check_alert_appear_5_sec(self) -> str:
        """Проверяем аллерт после 5 секунд."""
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check confirm alert')
    def check_confirm_alert(self) -> str:
        """Проверяем аллерт после выбора."""
        self.element_is_visible(self.locators.CONFIRM_BOX_AFTER_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        return self.element_is_present(self.locators.CONFIRM_RESULT).text

    @allure.step('check prompt alert')
    def check_prompt_alert(self) -> tuple:
        """Проверяем аллерт после ввода."""
        text = f'autotest{random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    """FramesPage."""

    locators = FramesPageLocators()

    @allure.step('check frame')
    def check_frame(self, frame_num: str) -> list:
        """Проверяем фрейм."""
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    """NestedFramesPage."""

    locators = NestedFramesLocators()

    @allure.step('check nested frame')
    def check_nested_frame(self) -> tuple:
        """Проверяем фрейм."""
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):
    """ModalDialogPage."""

    locators = ModalDialogPageLocators()

    @allure.step('check modal dialogs')
    def check_modal_dialogs(self) -> tuple:
        """Проверяем модальные окна."""
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]
