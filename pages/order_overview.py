from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderOverview(BasePage):
    page_url = '/shop/cart'

    def check_element_is_displayed(self):
        element = self.driver.find_element(By.CLASS_NAME, 'fa-shopping-cart')
        assert element.is_displayed()

    def check_is_enabled_element(self):
        element = self.driver.find_element(By.CLASS_NAME, 'fa-shopping-cart')
        assert element.is_enabled()
        # element.click()

    def check_element_text(self, text):
        element = self.driver.find_element(By.XPATH, '//*[@id="wrap"]/div[1]/div/div[3]/div/div[1]')
        assert element.text == text
