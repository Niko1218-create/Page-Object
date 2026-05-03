from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from pages.base_page import BasePage


class CategoryDesk(BasePage):
    page_url = '/shop/category/desks-1'

    def search_for_an_item_and_proceed_to_the_checkout_page(self):
        self.driver.implicitly_wait(6)
        desk = self.driver.find_element(By.CLASS_NAME, 'img-fluid')
        popup = self.driver.find_element(By.CLASS_NAME, 'a-submit')
        actions = ActionChains(self.driver)
        actions.move_to_element(desk)
        actions.click(popup)
        actions.perform()

    def verification_of_product_name_consistency_on_the_new_page(self, text):
        self.driver.implicitly_wait(6)
        new_page = self.driver.find_element(By.CLASS_NAME, 'product_display_name')
        assert new_page.text == text

    def entering_a_character_in_the_search_bar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(conditions.visibility_of_element_located((By.CLASS_NAME, 'multirange-wrapper')))
        search = self.driver.find_element(By.XPATH, '//*[@id="products_grid"]/div[1]/form/div/input')
        search.click()
        search.send_keys('D')
        wait = WebDriverWait(self.driver, 10)
        wait.until(conditions.visibility_of_element_located((By.CLASS_NAME, 'o_search_result_item_detail'))).click()

    def verification_that_the_selected_element_has_appeared_in_the_path(self, text):
        path = self.driver.find_element(By.XPATH, '//*[@id="products_grid"]/ol/li[2]/span')
        assert path.text == text

    def selecting_items_and_adding_to_cart(self):
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

    def checking_that_the_item_is_in_the_cart(self, text):
        element = self.driver.find_element(By.LINK_TEXT, 'Desk Stand with Screen')
        assert element.text == text
