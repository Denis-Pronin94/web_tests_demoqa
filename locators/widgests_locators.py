from selenium.webdriver.common.by import By


class AccordianPageLocators:
    """Локаторы для теста test_accordian."""

    SECTION_FIRST = (By.XPATH, '//div[@id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.XPATH, '//div[@id="section1Content"]//p')
    SECTION_SECOND = (By.XPATH, '//div[@id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.XPATH, '//div[@id="section2Content"]//p')
    SECTION_THIRD = (By.XPATH, '//div[@id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.XPATH, '//div[@id="section3Content"]//p')


class AutocompletePageLocators:
    """Локаторы для теста TestAutoComplete."""

    MULTI_INPUT = (By.XPATH, '//input[@id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (
        By.CSS_SELECTOR,
        'div[class="css-xb97g8 auto-complete__multi-value__remove"] svg path',
    )
    SINGLE_VALUE = (
        By.XPATH,
        '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]',
    )
    SINGLE_INPUT = (By.XPATH, '//input[@id="autoCompleteSingleInput"]')


class DatePickerPageLocators:
    """Локаторы для теста TestDatePiker."""

    DATE_INPUT = (By.XPATH, '//input[@id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (
        By.CSS_SELECTOR,
        'div[class^="react-datepicker__day react-datepicker__day"]',
    )

    DATE_AND_TIME_INPUT = (By.XPATH, '//input[@id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.XPATH, '//div[@class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.XPATH, '//div[@class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.XPATH, '//li[@class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.XPATH, '//div[@class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.XPATH, '//div[@class="react-datepicker__year-option"]')
