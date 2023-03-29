from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    """Локаторы для теста TestBrowserWindows."""

    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')
    TITLE_NEW = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')


class AlertsPageLocators:
    """Локаторы для теста TestAlerts."""

    SEE_ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.XPATH, '//button[@id="timerAlertButton"]')
    CONFIRM_BOX_AFTER_BUTTON = (By.XPATH, '//button[@id="confirmButton"]')
    PROMPT_BOX_ALERT_BUTTON = (By.XPATH, '//button[@id="promtButton"]')

    CONFIRM_RESULT = (By.XPATH, '//span[@id="confirmResult"]')
    PROMPT_RESULT = (By.XPATH, '//span[@id="promptResult"]')
