from selenium import webdriver
import pytest
from pages.category_desk import CategoryDesk
from pages.office_design import OfficeDesign
from pages.order_overview import OrderOverview


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def category_desk(driver):
    return CategoryDesk(driver)


@pytest.fixture()
def office_design(driver):
    return OfficeDesign(driver)


@pytest.fixture()
def order_overview(driver):
    return OrderOverview(driver)
