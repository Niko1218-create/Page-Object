def test_add_to_cart(office_design):
    office_design.open_pages()
    office_design.add_to_card()
    office_design.check_the_number_of_items_in_the_cart_is('1')


def test_removal_from_cart(office_design):
    office_design.open_pages()
    office_design.add_to_card()
    office_design.delete_product_from_cart()
    office_design.verify_cart_is_empty()


def test_search_bar(office_design):
    office_design.open_pages()
    office_design.entering_random_text_into_the_search_bar()
    office_design.result_verification('No results')
