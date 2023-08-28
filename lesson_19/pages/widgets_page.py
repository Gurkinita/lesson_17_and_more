
from locators import Locators

class WidgetsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_datepicker_button(self):
        self.driver.find_element(*Locators.DATEPICKER_BUTTON).click()

    def select_date(self):
        self.driver.find_element(*Locators.SELECTDATE_FIELD).click()
        self.driver.find_element(*Locators.MONTHSELECT_BUTTON).click()
        self.driver.find_element(*Locators.DECEMBER_BUTTON).click()
        self.driver.find_element(*Locators.YEARSELECT_BUTTON).click()
        self.driver.find_element(*Locators.DATESELECT_BUTTON).click()

    def select_datetime(self):
        self.driver.find_element(*Locators.DATEANDTIME_BUTTON).click()
        self.driver.find_element(*Locators.TIMESELECT_BUTTON).click()
