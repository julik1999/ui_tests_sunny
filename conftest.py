import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(r'C:/Users/User/PycharmProjects/ui tests sunny/chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()
