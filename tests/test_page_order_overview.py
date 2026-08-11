def test_cart_item_is_displayed(order_overview):
    order_overview.open_pages()
    order_overview.check_element_is_displayed()


def test_is_enabled_element(order_overview):
    order_overview.open_pages()
    order_overview.check_logo_click_returns_to_homepage('http://testshop.qa-practice.com/')


def test_that_the_cart_is_empty(order_overview):
    order_overview.open_pages()
    order_overview.check_element_text('Your cart is empty!')
