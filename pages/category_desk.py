from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from pages.base_page import BasePage
from locators.category_desk_locators import CategoryDeskLocators as Loc


class CategoryDesk(BasePage):
    page_url = '/shop/category/desks-1'

    def search_for_an_item_and_proceed_to_the_checkout_page(self):
        self.driver.implicitly_wait(6)
        desk = self.driver.find_element(*Loc.PRODUCT_IMAGE)
        popup = self.driver.find_element(*Loc.POPUP_SUBMIT)
        actions = ActionChains(self.driver)
        actions.move_to_element(desk)
        actions.click(popup)
        actions.perform()

    def verification_of_product_name_consistency_on_the_new_page(self, text):
        self.driver.implicitly_wait(6)
        new_page = self.driver.find_element(*Loc.PRODUCT_NAME_ON_NEW_PAGE)
        assert new_page.text == text

    def entering_a_character_in_the_search_bar(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(conditions.visibility_of_element_located(Loc.SEARCH_RESULTS_CONTAINER))
        search = self.driver.find_element(*Loc.SEARCH_INPUT)
        search.click()
        search.send_keys(text)
        wait = WebDriverWait(self.driver, 10)
        wait.until(conditions.visibility_of_element_located(Loc.SEARCH_RESULT_ITEM)).click()

    def verification_that_the_selected_element_has_appeared_in_the_path(self, text):
        path = self.driver.find_element(*Loc.BREADCRUMB_PATH)
        assert path.text == text

    def selecting_items_and_adding_to_cart(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        desk = self.driver.find_element(
            *Loc.DESK_STAND_PRODUCT
        )
        desk.click()
        plus = self.driver.find_element(*Loc.PLUS_BUTTON)
        actions = ActionChains(self.driver)
        actions.double_click(plus).perform()
        wait = WebDriverWait(self.driver, 10)
        button = self.driver.find_element(*Loc.ADD_TO_CART_BTN)
        button.click()
        wait.until(conditions.visibility_of_element_located(Loc.CART_QUANTITY_BADGE))
        basket = self.driver.find_element(*Loc.CART_LINK)
        basket.click()
        wait.until(conditions.visibility_of_element_located(Loc.CART_ITEM_LINK))

    def checking_that_the_item_is_in_the_cart(self, text):
        element = self.driver.find_element(*Loc.CART_ITEM_TEXT)
        assert element.text == text
