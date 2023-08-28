
from locators import Locators

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver

    def is_button_visible(self):
        try:
            button = self.driver.find_element(*Locators.BUTTONS_BUTTON)
            return button.is_displayed()
        except:
            return False

    def click_clickme_button(self):
        clickme_button = self.driver.find_element(*Locators.CLICKME_BUTTON)
        clickme_button.click()

    def is_dynamic_message_visible(self):
        try:
            message_element = self.driver.find_element(*Locators.CLICKME_RESULT)
            return message_element.is_displayed()
        except:
            return False

    def click_radio_button(self):
        radio_button = self.driver.find_element(*Locators.RADIO_BUTTON)
        radio_button.click()

    def click_yes_button(self):
        clickme_button = self.driver.find_element(*Locators.YES_BUTTON)
        clickme_button.click()

    def is_clickme_result_visible(self):
        try:
            message_element = self.driver.find_element(*Locators.CLICKME_RESULT)
            return message_element.is_displayed()
        except:
            return False

    def is_yes_text_visible(self):
        try:
            message_element = self.driver.find_element(*Locators.YES_TEXT)
            return message_element.is_displayed()
        except:
            return False