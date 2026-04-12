
from pages.order_overview import OrderOverview
from pages.category_desk import CategoryDesk
from pages.office_design import OfficeDesign


def test_element(driver):
    order_overview = OrderOverview(driver)
    order_overview.open_pages()
    order_overview.element_is_displayed()


def test_click_element(driver):
    order_overview = OrderOverview(driver)
    order_overview.open_pages()
    order_overview.click_element()


def test_element_text(driver):
    order_overview = OrderOverview(driver)
    order_overview.open_pages()
    order_overview.element_text()


def test_desk(driver):
    category_desk = CategoryDesk(driver)
    category_desk.open_pages()
    category_desk.new_page_text()


def test_search_field(driver):
    category_desk = CategoryDesk(driver)
    category_desk.open_pages()
    category_desk.desk_text()


def test_scroll(driver):
    category_desk = CategoryDesk(driver)
    category_desk.open_pages()
    category_desk.element_text()


def test_basket(driver):
    office_desigh = OfficeDesign(driver)
    office_desigh.open_pages()
    office_desigh.element_text()


def test_removal_from_cart(driver):
    office_desigh = OfficeDesign(driver)
    office_desigh.open_pages()
    office_desigh.element_text_matches()


def test_search_bar(driver):
    office_desigh = OfficeDesign(driver)
    office_desigh.open_pages()
    office_desigh.no_result()
