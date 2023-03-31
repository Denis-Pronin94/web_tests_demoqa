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


class FramesPageLocators:
    """Локаторы для теста test_frames."""

    FIRST_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    SECOND_FRAME = (By.XPATH, '//iframe[@id="frame2"]')
    TITLE_FRAME = (By.XPATH, '//h1[@id="sampleHeading"]')


class NestedFramesLocators:
    """Локаторы для теста test_nested_frames."""

    PARENT_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogPageLocators:
    """Локаторы для теста test_modal_dialog."""

    SMALL_MODAL_BUTTON = (By.XPATH, '//button[@id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.XPATH, '//button[@id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.XPATH, '//div[@class="modal-body"]')
    TITLE_SMALL_MODAL = (By.XPATH, '//div[@id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.XPATH, '//button[@id="showLargeModal"]')
    # LARGE_MODAL_CLOSE_BUTTON = (By.XPATH, '//button[@id="closeLargeModal"]')
    BODY_LARGE_MODAL = (By.XPATH, '//div[@class="modal-body"]')
    TITLE_LARGE_MODAL = (By.XPATH, '//div[@id="example-modal-sizes-title-lg"]')
