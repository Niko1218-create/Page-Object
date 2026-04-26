def test_element_is_displayed(order_overview):
    order_overview.open_pages()
    order_overview.check_element_is_displayed()


def test_is_enabled_element(order_overview):
    order_overview.open_pages()
    order_overview.check_is_enabled_element()


def test_element_text(order_overview):
    order_overview.open_pages()
    order_overview.check_element_text('Your cart is empty!')


def test_new_page_text(category_desk):
    category_desk.open_pages()
    category_desk.checking_product_page_title('[FURN_0096] Customizable Desk (Steel, White)')


def test_search_field(category_desk):
    category_desk.open_pages()
    category_desk.open_page_by_search_and_verify()


def test_scroll(category_desk):
    category_desk.open_pages()
    category_desk.check_element_text()


def test_basket(office_design):
    office_design.open_pages()
    office_design.add_to_cart_and_check_quantity_in_cart()


def test_removal_from_cart(office_design):
    office_design.open_pages()
    office_design.add_to_cart_and_then_delete_and_verify_cart_is_empty()


def test_search_bar(office_design):
    office_design.open_pages()
    office_design.check_empty_search_results()
