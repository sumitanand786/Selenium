import pytest
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from testdata.HomePageData import HomePageData


class Test_homepage(BaseClass):
    def test_home(self, test_data):
        homepage = HomePage(self.driver)
        homepage.name().send_keys(test_data["Firstname"])
        homepage.email().send_keys(test_data["Email"])
        homepage.password().send_keys(test_data["Password"])
        homepage.check_box().click()
        gender_dropdown = Select(homepage.gender())
        gender_dropdown.select_by_visible_text("Male")
        homepage.employee().click()
        homepage.message_button().click()
        success_message = homepage.message_capture().text
        print(success_message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def test_data(self, request):
        return request.param
