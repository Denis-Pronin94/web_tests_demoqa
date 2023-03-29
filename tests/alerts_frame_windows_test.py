from pages.alerts_frame_windows_page import BrowserWindowPage

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
