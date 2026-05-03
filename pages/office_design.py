from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from pages.base_page import BasePage


class OfficeDesign(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def add_to_card(self):
        self.driver.find_element(By.ID, 'add_to_cart').click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(conditions.text_to_be_present_in_element((By.CLASS_NAME, 'my_cart_quantity'), '1'))

    def check_the_number_of_items_in_the_cart_is(self, number):
        element = self.driver.find_element(By.CLASS_NAME, 'my_cart_quantity')
        assert element.text == number

    def delete_product_from_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'o_navlink_background').click()
        self.driver.find_element(By.XPATH, '//*[@id="cart_products"]/div/div[3]/div[1]/a[1]').click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            conditions.invisibility_of_element_located((By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a/div/sup')))

    def verify_cart_is_empty(self):
        element = self.driver.find_element(By.CLASS_NAME, 'js_cart_lines')
        assert element.text == 'Your cart is empty!'

    def entering_random_text_into_the_search_bar(self):
        field = self.driver.find_element(By.XPATH, '//*[@id="product_detail"]/div[1]/div[1]/div/form/div/input')
        field.click()
        field.send_keys('gdhtdz')
        button = self.driver.find_element(By.XPATH, '//*[@id="product_detail"]/div[1]/div[1]/div/form/div/button')
        button.click()
        self.driver.implicitly_wait(5)

    def result_verification(self, text):
        result = self.driver.find_element(By.CLASS_NAME, 'mt8')
        assert result.text == text
