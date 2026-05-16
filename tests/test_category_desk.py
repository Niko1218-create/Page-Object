def test_new_page_text(category_desk):
    category_desk.open_pages()
    category_desk.search_for_an_item_and_proceed_to_the_checkout_page()
    category_desk.verification_of_product_name_consistency_on_the_new_page(
        '[FURN_0096] Customizable Desk (Steel, White)'
    )


def test_search_field(category_desk):
    category_desk.open_pages()
    category_desk.entering_a_character_in_the_search_bar('D')
    category_desk.verification_that_the_selected_element_has_appeared_in_the_path('Desks')


def test_scroll(category_desk):
    category_desk.open_pages()
    category_desk.selecting_items_and_adding_to_cart()
    category_desk.checking_that_the_item_is_in_the_cart('Desk Stand with Screen')
