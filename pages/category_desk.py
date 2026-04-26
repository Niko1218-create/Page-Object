from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from pages.base_page import BasePage


class CategoryDesk(BasePage):
    page_url = '/shop/category/desks-1'

    def checking_product_page_title(self, text):
        self.driver.implicitly_wait(6)
        desk = self.driver.find_element(By.CLASS_NAME, 'img-fluid')
        popup = self.driver.find_element(By.CLASS_NAME, 'a-submit')
        actions = ActionChains(self.driver)
        actions.move_to_element(desk)
        actions.click(popup)
        actions.perform()
        new_page = self.driver.find_element(By.CLASS_NAME, 'product_display_name')
        assert new_page.text == text

    def open_page_by_search_and_verify(self):
        search = self.driver.find_element(By.XPATH, '//*[@id="products_grid"]/div[1]/form/div/input')
        search.send_keys('Desks')
        glass = self.driver.find_element(By.CLASS_NAME, 'oi-search')
        glass.click()
        desk = self.driver.find_element(By.CLASS_NAME, 'd-inline-block')
        assert desk.text == 'Desks'

    def check_element_text(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        desk = self.driver.find_element(
            By.XPATH,

            '//*[@id="products_grid"]/div[3]/table/tbody/tr[3]/td/div/form/div[1]/a/span[1]/img'
        )

        desk.click()
        plus = self.driver.find_element(By.CLASS_NAME, 'fa-plus')
        actions = ActionChains(self.driver)
        actions.double_click(plus).perform()
        wait = WebDriverWait(self.driver, 10)
        button = self.driver.find_element(By.ID, 'add_to_cart')
        button.click()
        wait.until(conditions.visibility_of_element_located((By.CLASS_NAME, 'my_cart_quantity')))
        basket = self.driver.find_element(By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a')
        basket.click()
        wait.until(conditions.visibility_of_element_located((By.LINK_TEXT, 'Desk Stand with Screen')))
        element = self.driver.find_element(By.LINK_TEXT, 'Desk Stand with Screen')
        assert element.text == 'Desk Stand with Screen'
