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
