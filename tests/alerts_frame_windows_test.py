from pages.alerts_frame_windows_page import AlertsPage, BrowserWindowPage

from selenium import webdriver


class TestAlertsFrameWindows:
    """Сьют - TestAlertsFrameWindows."""

    class TestBrowserWindows:
        """Тест - TestBrowserWindows."""

        def test_new_tab(self, driver: webdriver):
            """Тест - text_box."""
            browser_window = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window.open()
            text_result = browser_window.check_opened_new_tab()
            assert text_result == 'This is a sample page'

        def test_new_window(self, driver: webdriver):
            """Тест - text_box."""
            browser_window = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window.open()
            text_result = browser_window.check_opened_new_window()
            assert text_result == 'This is a sample page'

    class TestAlerts:
        """Тест - TestAlerts."""

        def test_see_alert(self, driver: webdriver):
            """Тест - test_see_alert."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            alert_text = alert.check_see_alert()
            assert alert_text == 'You clicked a button'

        def test_alert_appear_5_sec(self, driver: webdriver):
            """Тест - test_alert_appear_5_sec."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            alert_text = alert.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_confirm_alert(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            alert_text = alert.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_prompt_alert(self, driver: webdriver):
            """Тест - test_confirm_alert."""
            alert = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert.open()
            text, alert_text = alert.check_prompt_alert()
            assert alert_text == f'You entered {text}'