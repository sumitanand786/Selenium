from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        obj_ser = Service()
        driver = webdriver.Chrome(service=obj_ser, options=options)
    elif browser_name=="firefox":
        obj_ser = Service()
        driver = webdriver.Firefox(service=obj_ser)
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
