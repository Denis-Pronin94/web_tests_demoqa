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
    """Локаторы для теста TestRadioButton."""

    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@aria-label="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (
        By.XPATH, '//span[@class="rct-checkbox"]//*[@class="rct-icon rct-icon-check"]',
    )
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class RadioButtonPageLocators:
    """Локаторы для теста TestCheckBox."""

    YES_RADIO_BUTTON = (By.XPATH, '//label[@class="custom-control-label"][@for="yesRadio"]')
    IMPRESSIVE_RADIO_BUTTON = (
        By.XPATH,
        '//label[@class="custom-control-label"][@for="impressiveRadio"]',
    )
    NO_RADIO_BUTTON = (By.XPATH, '//label[@class="custom-control-label disabled"][@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class WebTablePageLocators:
    """Локаторы для теста TestCheckBox."""

    ADD_BUTTON = (By.XPATH, '//button[@id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]')
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')

    SEARCH_WORLD = (By.XPATH, '//input[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'

    UPDATE_BUTTON = (By.XPATH, '//span[@title="Edit"]')

    NO_ROWS_FOUND = (By.XPATH, '//div[@class="rt-noData"]')

    COUNT_ROW_LIST = (By.XPATH, '//select[@aria-label="rows per page"]')


class ButtonPageLocators:
    """Локаторы для теста TestButton."""

    DOUBLE_BUTTON = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[@class="mt-4"][2]//button')

    SUCCESS_DOUBLE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.XPATH, '//p[@id="rightClickMessage"]')
    SUCCESS_ME_BUTTON = (By.XPATH, '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:
    """Локаторы для теста TestLinks."""

    SIMPLE_LINK = (By.XPATH, '//a[@id="simpleLink"]')
    BAD_REQEST = (By.XPATH, '//a[@id="bad-request"]')


class UploadAndDownloadPageLocators:
    """Локаторы для теста test_upload_file."""

    UPLOAD_FILE = (By.XPATH, '//input[@id="uploadFile"]')
    UPLOADED_RESULT = (By.XPATH, '//p[@id="uploadedFilePath"]')

    DOWNLOAD_FILE = (By.XPATH, '//a[@id="downloadButton"]')
