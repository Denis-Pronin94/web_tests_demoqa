from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """Локаторы для теста TestTextBox."""

    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//div[@class="text-right col-md-2 col-sm-12"]')

    CREATED_FULL_NAME = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:
    """Локаторы для теста TestCheckBox."""

    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@aria-label="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (
        By.XPATH, '//span[@class="rct-checkbox"]//*[@class="rct-icon rct-icon-check"]',
    )
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')
