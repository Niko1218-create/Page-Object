from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from pages.base_page import BasePage
from locators.office_design_locators import OfficeDesignLocators as Loc


class OfficeDesign(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def add_to_card(self):
        self.driver.find_element(*Loc.ADD_TO_CART_BTN).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(conditions.text_to_be_present_in_element(Loc.CART_QUANTITY_BADGE, '1'))

    def check_the_number_of_items_in_the_cart_is(self, number):
        element = self.driver.find_element(*Loc.CART_QUANTITY_BADGE)
        assert element.text == number

    def delete_product_from_cart(self):
        self.driver.find_element(*Loc.NAV_BACK_BTN).click()
        self.driver.find_element(*Loc.REMOVE_ITEM_BTN).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(conditions.invisibility_of_element_located(Loc.CART_QUANTITY_BADGE))

    def verify_cart_is_empty(self):
        element = self.driver.find_element(*Loc.CART_CONTENT)
        assert element.text == 'Your cart is empty!'

    def entering_random_text_into_the_search_bar(self):
        field = self.driver.find_element(*Loc.SEARCH_INPUT)
        field.click()
        field.send_keys('gdhtdz')
        button = self.driver.find_element(*Loc.SEARCH_BUTTON)
        button.click()
        self.driver.implicitly_wait(5)

    def result_verification(self, text):
        result = self.driver.find_element(*Loc.SEARCH_RESULT)
        assert result.text == text
