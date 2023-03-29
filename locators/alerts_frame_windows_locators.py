from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    """Локаторы для теста TestBrowserWindows."""

    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')
    TITLE_NEW = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')
