from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # для Докера
import pytest
from pages.category_desk import CategoryDesk
from pages.office_design import OfficeDesign
from pages.order_overview import OrderOverview


@pytest.fixture()
def driver():
    options = Options()  # для Докера
    options.add_argument('--headless')  # для Докера
    options.add_argument('--no-sandbox')  # для Докера
    options.add_argument('--disable-dev-shm-usage')  # для Докера
    options.add_argument('--disable-gpu')  # для Докера
    options.add_argument('--window-size=1920,1080')  # ВСТАВЬТЕ ЭТУ СТРОЧКУ
    chrome_driver = webdriver.Chrome(options=options)  # для Докера
    # chrome_driver.maximize_window()
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
