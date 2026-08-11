from pages.base_page import BasePage
from locators.order_overview_locators import OrderOverviewLocators as Loc


class OrderOverview(BasePage):
    page_url = '/shop/cart'

    def check_element_is_displayed(self):
        element = self.driver.find_element(*Loc.CART_ICON)
        assert element.is_displayed()

    def check_logo_click_returns_to_homepage(self, url):
        element = self.driver.find_element(*Loc.LOGO)
        element.click()
        assert self.driver.current_url == url

    def check_element_text(self, text):
        element = self.driver.find_element(*Loc.EMPTY_CART_TEXT)
        assert element.text == text
