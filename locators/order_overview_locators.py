from selenium.webdriver.common.by import By


class OrderOverviewLocators:
    CART_ICON = (By.CLASS_NAME, 'fa-shopping-cart')
    LOGO = (By.CLASS_NAME, 'img-fluid')
    EMPTY_CART_TEXT = (By.XPATH, '//*[contains(text(), "Your cart is empty")]')
