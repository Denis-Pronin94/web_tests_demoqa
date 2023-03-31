from selenium.webdriver.common.by import By


class SortablePageLocators:
    """Локаторы для теста test_sortable."""

    TAB_LIST = (By.XPATH, '//div[@id="demo-tabpane-list"]')
    LIST_ITEM = (By.XPATH, '//div[@id="demo-tabpane-list"]/div/div')
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//div[@id="demo-tabpane-grid"]/div/div/div')


class SelectablePageLocators:
    """Локаторы для теста test_selectable."""

    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//li[@class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (
        By.XPATH,
        '//li[@class="mt-2 list-group-item active list-group-item-action"]',
    )
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//li[@class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.XPATH, '//li[@class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    """Локаторы для теста test_resizable."""

    RESIZABLE_BOX_HANDLE = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]/span')
    RESIZABLE_BOX = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.XPATH, '//div[@id="resizable"]/span')
    RESIZABLE = (By.XPATH, '//div[@id="resizable"]')


class DroppablePageLocators:
    """Локаторы для теста TestDroppable."""

    SIMPLE_TAB = (By.XPATH, '//a[@id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.XPATH, '//div[@id="draggable"]')
    DROP_HERE_SIMPLE = (By.XPATH, '//div[@id="simpleDropContainer"]/div[@id="droppable"]')

    ACCEPT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.XPATH, '//div[@id="acceptable"]')
    NOT_ACCEPTABLE = (By.XPATH, '//div[@id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.XPATH, '//div[@id="acceptDropContainer"]/div[@id="droppable"]')

    PREVENT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.XPATH, '//div[@id="notGreedyDropBox"]/p')
    NOT_GREEDY_INNER_BOX = (By.XPATH, '//div[@id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.XPATH, '//div[@id="greedyDropBox"]/p')
    GREEDY_INNER_BOX = (By.XPATH, '//div[@id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.XPATH, '//div[@id="dragBox"]')

    REVERT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.XPATH, '//div[@id="revertable"]')
    NOT_REVERT = (By.XPATH, '//div[@id="notRevertable"]')
    DROP_HERE_REVERT = (By.XPATH, '//div[@id="revertableDropContainer"]/div[@id="droppable"]')


class DraggablePageLocators:
    """Локаторы для теста TestDraggable."""

    SIMPLE_TAB = (By.XPATH, '//a[@id="draggableExample-tab-simple"]')
    DRAG_ME = (By.XPATH, '//div[@id="dragBox"]')

    AXIS_TAB = (By.XPATH, '//a[@id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.XPATH, '//div[@id="restrictedX"]')
    ONLY_Y = (By.XPATH, '//div[@id="restrictedY"]')
