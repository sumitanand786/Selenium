from selenium.webdriver.common.by import By


class CheckOutPage:
    available_products = (By.XPATH, "//app-card-list/app-card/div[@class='card h-100']")
    button_checkout=(By.CSS_SELECTOR, ".btn-primary")
    button_final_checkout=(By.CSS_SELECTOR, "button[class*='success']")

    def __init__(self, driver):
        self.driver=driver

    def all_products(self):
        return self.driver.find_elements(*CheckOutPage.available_products)

    def checkout_click(self):
        return self.driver.find_element(*CheckOutPage.button_checkout).click()

    def final_checkout_click(self):
        return self.driver.find_element(*CheckOutPage.button_final_checkout).click()
