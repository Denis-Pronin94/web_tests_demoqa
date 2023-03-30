from selenium.webdriver.common.by import By


class SortablePageLocators:
    """Локаторы для теста test_sortable."""

    TAB_LIST = (By.XPATH, '//div[@id="demo-tabpane-list"]')
    LIST_ITEM = (By.XPATH, '//div[@id="demo-tabpane-list"]/div/div')
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//div[@id="demo-tabpane-grid"]/div/div/div')
