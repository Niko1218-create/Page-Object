from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderOverview(BasePage):
    page_url = '/shop/cart'

    def element_is_displayed(self):
        element = self.driver.find_element(By.CLASS_NAME, 'fa-shopping-cart')
        assert element.is_displayed()

    def click_element(self):
        element = self.driver.find_element(By.CLASS_NAME, 'fa-shopping-cart')
        assert element.is_enabled()
        element.click()

    def element_text(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[1]/div/div[3]/div/div[1]')
        assert element.text == 'Your cart is empty!'
