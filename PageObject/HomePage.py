from selenium.webdriver.common.by import By

from PageObject.CheckOutPage import CheckOutPage


class HomePage:
    # self.driver.find_element(By.LINK_TEXT, "Shop").click()
    button_shop = (By.LINK_TEXT, "Shop")
    text_box_name = (By.CSS_SELECTOR, "input[name='name']:nth-child(2)")
    text_box_email = (By.XPATH, "//input[@name='email']")
    text_box_password = (By.ID, "exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    radio_status = (By.CSS_SELECTOR, "#inlineRadio2")
    button_submit = (By.CSS_SELECTOR, ".btn-success")
    success_message = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shop(self):
        self.driver.find_element(*HomePage.button_shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def name(self):
        return self.driver.find_element(*HomePage.text_box_name)

    def email(self):
        return self.driver.find_element(*HomePage.text_box_email)

    def password(self):
        return self.driver.find_element(*HomePage.text_box_password)

    def check_box(self):
        return self.driver.find_element(*HomePage.checkbox)

    def gender(self):
        return self.driver.find_element(*HomePage.gender_dropdown)

    def employee(self):
        return self.driver.find_element(*HomePage.radio_status)

    def message_button(self):
        return self.driver.find_element(*HomePage.button_submit)

    def message_capture(self):
        return self.driver.find_element(*HomePage.success_message)

