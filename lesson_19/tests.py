import unittest
import pytest
import time
import allure
from selenium import webdriver
from lesson_19.pages.elements_page import ElementsPage
from lesson_19.pages.widgets_page import WidgetsPage
from lesson_19.pages.text_box_page import TextBoxPage

class TestElementsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/elements")
        self.driver.implicitly_wait(2)
        self.elements_page = ElementsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.feature("Elements Page")
    @allure.story("Button Visibility")
    def test_button_visibility(self):
        with allure.step("Check if button is visible"):
            self.assertTrue(self.elements_page.is_button_visible(), "Кнопка не видима.")

    @allure.feature("Elements Page")
    @allure.story("ClickMe Button")
    def test_clickme_button(self):
        self.driver.get("https://demoqa.com/buttons")
        time.sleep(2)
        with allure.step("Click on ClickMe button"):
            self.elements_page.click_clickme_button()
        time.sleep(2)
        with allure.step("Check if ClickMe result is visible"):
            self.assertTrue(self.elements_page.is_clickme_result_visible(), "Кнопка не видима.")

    @allure.feature("Elements Page")
    @allure.story("Yes Button")
    def test_yes_button(self):
        self.driver.get("https://demoqa.com/elements")
        time.sleep(2)
        with allure.step("Click on radio button"):
            self.elements_page.click_radio_button()
        time.sleep(2)
        with allure.step("Click on Yes button"):
            self.elements_page.click_yes_button()
        time.sleep(2)
        with allure.step("Check if Yes text is visible"):
            self.assertTrue(self.elements_page.is_yes_text_visible(), "Кнопка не видима.")

class TestWidgetsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/date-picker")
        self.driver.maximize_window()
        self.widgets_page = WidgetsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.feature("Widgets Page")
    @allure.story("Date and DateTime Picker")
    def test_datepicker_and_datetimepicker(self):
        with allure.step("Select a date"):
            self.widgets_page.select_date()
        time.sleep(2)
        with allure.step("Select a date and time"):
            self.widgets_page.select_datetime()
        time.sleep(2)

class TestTextBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.textbox_page = TextBoxPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @allure.feature("Text Box Page")
    @allure.story("Text Box Submission")
    def test_textbox_submission(self):
        self.driver.get("https://demoqa.com/text-box")
        self.driver.set_window_size(1920, 1080)

        username = "Julia Rodenkova"
        useremail = "musicien0070@gmail.com"
        current_address = "Sofia Bulgaria"
        permanent_address = "Odessa Sweet Home"

        with allure.step("Enter user details"):
            self.textbox_page.enter_username(username)
            self.textbox_page.enter_useremail(useremail)
            self.textbox_page.enter_current_address(current_address)
            self.textbox_page.enter_permanent_address(permanent_address)
            self.textbox_page.click_submit_button()

        with allure.step("Verify output text"):
            output_text = self.textbox_page.get_output_text()
            assert "Name:" in output_text
            assert "Email:" in output_text
            assert "Current Address :" in output_text
            assert "Permananet Address :" in output_text

if __name__ == "__main__":
    unittest.main()
#  тут какое-то изменение кода
#  тут какое-то изменение кода
#  тут какое-то изменение кода
#  тут какое-то изменение кода


#  тут какое-то изменение кода#  тут какое-то изменение кода#  тут какое-то изменение кода

#  тут какое-то изменение кода
