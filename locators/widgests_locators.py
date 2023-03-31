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


class SliderPageLocators:
    """Локаторы для теста test_slider."""

    INPUT_SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.XPATH, '//input[@id="sliderValue"]')


class ProgressBarPageLocators:
    """Локаторы для теста test_progress_bar."""

    PROGRESS_BAR_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.XPATH, '//div[@class="progress-bar bg-info"]')


class TabsPageLocators:
    """Локаторы для теста test_tabs."""

    TABS_WHAT = (By.XPATH, '//a[@id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.XPATH, '//a[@id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-origin"]')
    TABS_USE = (By.XPATH, '//a[@id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-use"]')
    TABS_MORE = (By.XPATH, '//a[@id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    """Локаторы для теста test_tool_tips."""

    BUTTON = (By.XPATH, '//button[@id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.XPATH, '//button[@aria-describedby="buttonToolTip"]')

    FIELD = (By.XPATH, '//input[@id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.XPATH, '//input[@aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//a[text()="Contrary"]')
    TOOL_TIP_CONTRARY = (By.XPATH, '//a[@aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//a[text()="1.10.32"]')
    TOOL_TIP_SECTION = (By.XPATH, '//a[@aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.XPATH, '//div[@class="tooltip-inner"]')


class MenuPageLocators:
    """Локаторы для теста test_menu."""

    MENU_ITEM_LIST = (By.XPATH, '//ul[@id="nav"]//li//a')
