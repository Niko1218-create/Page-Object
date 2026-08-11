from selenium.webdriver.common.by import By


class OfficeDesignLocators:
    ADD_TO_CART_BTN = (By.ID, 'add_to_cart')
    CART_QUANTITY_BADGE = (By.CLASS_NAME, 'my_cart_quantity')
    NAV_BACK_BTN = (By.CLASS_NAME, 'o_navlink_background')
    REMOVE_ITEM_BTN = (By.XPATH, '//a[@title="Remove one"]')
    CART_CONTENT = (By.CLASS_NAME, 'js_cart_lines')
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[contains(text(), "Your cart is empty")]')
    SEARCH_INPUT = (By.CSS_SELECTOR, '#product_detail input[type="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#product_detail button[type="submit"]')
    SEARCH_RESULT = (By.CLASS_NAME, 'mt8')
