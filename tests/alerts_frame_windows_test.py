import allure

from pages.alerts_frame_windows_page import (
    AlertsPage,
    BrowserWindowPage,
    FramesPage,
    ModalDialogPage,
    NestedFramesPage,
)

from selenium import webdriver


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindows:
    """Сьют - TestAlertsFrameWindows."""

    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        """Тест - TestBrowserWindows."""

        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver: webdriver):
            """Тест - text_box."""
            browser_window = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window.open()
            text_result = browser_window.check_opened_new_tab()
            assert text_result == 'This is a sample page'

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver: webdriver):
            """Тест - text_box."""
            browser_window = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window.open()
            text_result = browser_window.check_opened_new_window()
            assert text_result == 'This is a sample page'

    @allure.feature('Alerts Page')
    class TestAlerts:
        """Тест - TestAlerts."""

        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver: webdriver):
            """Тест - test_see_alert."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            alert_text = alert.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_5_sec(self, driver: webdriver):
            """Тест - test_alert_appear_5_sec."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            alert_text = alert.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            alert_text = alert.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            text, alert_text = alert.check_prompt_alert()
            assert alert_text == f'You entered {text}'

    @allure.feature('Frame Page')
    class TestFrames:
        """Тест - TestFrames."""

        @allure.title('Check the page with frames')
        def test_frames(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            frames = FramesPage(driver, 'https://demoqa.com/frames')
            frames.open()
            result_frame1 = frames.check_frame('frame1')
            result_frame2 = frames.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px']
            assert result_frame2 == ['This is a sample page', '100px', '100px']

    @allure.feature('Nested Page')
    class TestNestedFrames:
        """Тест - TestFrames."""

        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            nested_frames = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames.open()
            parent_text, child_text = nested_frames.check_nested_frame()
            assert parent_text == 'Parent frame'
            assert child_text == 'Child Iframe'

    @allure.feature('Modal Dialog Page')
    class TestModalDialog:
        """Тест - TestModalDialog."""

        @allure.title('Check the page with modal dialogs')
        def test_modal_dialog(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            modal_dialog = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog.open()
            small, large = modal_dialog.check_modal_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'
