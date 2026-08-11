from selenium.webdriver.common.by import By


class CategoryDeskLocators:
    PRODUCT_IMAGE = (By.CLASS_NAME, 'img-fluid')
    POPUP_SUBMIT = (By.CLASS_NAME, 'a-submit')
    PRODUCT_NAME_ON_NEW_PAGE = (By.CLASS_NAME, 'product_display_name')
    SEARCH_RESULTS_CONTAINER = (By.CLASS_NAME, 'multirange-wrapper')
    SEARCH_INPUT = (By.XPATH, '//*[@id="products_grid"]/div[1]/form/div/input')
    SEARCH_RESULT_ITEM = (By.CLASS_NAME, 'o_search_result_item_detail')
    BREADCRUMB_PATH = (By.XPATH, '//*[@id="products_grid"]/ol/li[2]/span')
    DESK_STAND_PRODUCT = (By.XPATH, '//img[contains(@alt, "FURN_7888")]')
    PLUS_BUTTON = (By.CLASS_NAME, 'fa-plus')
    ADD_TO_CART_BTN = (By.ID, 'add_to_cart')
    CART_QUANTITY_BADGE = (By.CLASS_NAME, 'my_cart_quantity')
    CART_LINK = (By.XPATH, '//a[contains(@href, "cart")]')
    CART_ITEM_LINK = (By.LINK_TEXT, 'Desk Stand with Screen')
    CART_ITEM_TEXT = (By.XPATH, '//*[contains(text(), "Desk Stand with Screen")]')
