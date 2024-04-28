from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import ConfirmPage
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_ecommerce_flow(self):
        log=self.getLogger()

        actual_title = self.driver.title
        if actual_title == "ProtoCommerce":
            assert True
        else:
            assert False, "Page title does not match"
        homepage=HomePage(self.driver)
        check_out_page=homepage.shop()
        log.info("getting all the cart titles")
        products = check_out_page.all_products()
        print("Total products are: ", len(products))

        for product in products:
            product_name_element = product.find_element(By.XPATH, "div/h4")
            product_name = product_name_element.text
            log.info(product_name)
            if product_name == "Blackberry":
                button = product.find_element(By.XPATH, "div/button")
                button.click()
                log.info("Blackberry added to cart successfully")
        check_out_page.checkout_click()
        check_out_page.final_checkout_click()
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        self.dynamic_dropdown("India")
        log.info("Entering country name")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        confirm_page=ConfirmPage(self.driver)
        confirm_page.checkbox_click()
        confirm_page.purchase_click()
        success_message = confirm_page.capture_message()
        print(success_message)
        assert "Success! Thank you" in success_message
        log.info("Assertion passed, text matched")
