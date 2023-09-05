
from locators import Locators

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*Locators.USERNAME_FIELD).send_keys(username)

    def enter_useremail(self, useremail):
        self.driver.find_element(*Locators.USEREMAIL_FIELD).send_keys(useremail)

    def enter_current_address(self, current_address):
        self.driver.find_element(*Locators.CURRENTADDRESS_FIELD).send_keys(current_address)

    def enter_permanent_address(self, permanent_address):
        self.driver.find_element(*Locators.PERMANENTADDRESS_FIELD).send_keys(permanent_address)

    def click_submit_button(self):
        self.driver.find_element(*Locators.SUBMIT_BUTTON).click()

    def get_output_text(self):
        output_div = self.driver.find_element(*Locators.OUTPUT_DIV)
        return output_div.text
#  тут какое-то изменение кода
#  тут какое-то изменение кода
#  тут какое-то изменение кода
#  тут какое-то изменение кода
#  тут какое-то изменение кода