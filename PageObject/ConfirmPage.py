from selenium.webdriver.common.by import By


class ConfirmPage:
    checkbox_agree = (By.CSS_SELECTOR, "label[for='checkbox2']")
    button_purchase=(By.XPATH, "//input[@value='Purchase']")
    text_message=(By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def checkbox_click(self):
        return self.driver.find_element(*ConfirmPage.checkbox_agree).click()

    def purchase_click(self):
        return self.driver.find_element(*ConfirmPage.button_purchase).click()

    def capture_message(self):
        return self.driver.find_element(*ConfirmPage.text_message).text
