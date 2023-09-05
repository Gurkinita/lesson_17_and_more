import pytest
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import allure


# 123
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("добавление нового пользователя")
@allure.feature("Развод на деньги")
@allure.story("добавление юзера")
@allure.severity(allure.severity_level.CRITICAL)
def test_1(browser):
    browser.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    browser.set_window_size(1920, 1080)

    wait = WebDriverWait(browser, 10)
    bank_manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")))
    bank_manager_login_btn.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(1)")))

    transfer_btn = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(1)")
    transfer_btn.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input")))

    input_field1 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input")
    input_field1.send_keys("ЮЛИЯ")
    time.sleep(2)

    input_field2 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input")
    input_field2.send_keys("Reach bitch")
    time.sleep(2)

    input_field3 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input")
    input_field3.send_keys("65000")
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button")
    button.click()
    time.sleep(2)


@allure.title("проверить валюту Гарри")
@allure.feature("проверка валюты")
@allure.story("открыть пользователя Гарри")
@allure.severity(allure.severity_level.BLOCKER)
def test_2(browser):
    browser.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    browser.set_window_size(1920, 1080)

    wait = WebDriverWait(browser, 10)
    bank_manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")))
    bank_manager_login_btn.click()
    time.sleep(1)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(2)")))

    open_account_btn = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(2)")
    open_account_btn.click()
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#userSelect")))
    time.sleep(1)

    select_user = Select(browser.find_element(By.CSS_SELECTOR, "#userSelect"))
    select_user.select_by_index(2)
    time.sleep(1)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#currency")))
    time.sleep(1)

    select_currency = Select(browser.find_element(By.CSS_SELECTOR, "#currency"))
    select_currency.select_by_index(3)
    time.sleep(1)

    submit_btn = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button")
    submit_btn.click()


@allure.title("открыть список пользователей")
@allure.feature("админ логин")
@allure.story("список пользователей")
@allure.severity(allure.severity_level.NORMAL)
def test_3(browser):
    browser.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    browser.set_window_size(1920, 1080)

    wait = WebDriverWait(browser, 10)
    bank_manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")))
    bank_manager_login_btn.click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.center > button:nth-child(3)")))

    button_3 = browser.find_element(By.CSS_SELECTOR,
                                    "body > div > div > div.ng-scope > div > div.center > button:nth-child(3)")
    button_3.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button"))) # noqa

    table_button = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button") # noqa
    table_button.click()


class Test4():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title('чекбоксы')
    @allure.feature("жмакни на кнопку")
    @allure.story("тут сторя")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_4(self):
        self.driver.get("http://uitestingplayground.com/home")
        self.driver.set_window_size(1920, 1080)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Click").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "badButton").click()
        time.sleep(2)


class Test5():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title('ползунки')
    @allure.feature("жмакни на кнопку")
    @allure.story("скрытая кнопка")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_5(self):
        self.driver.get("http://uitestingplayground.com/home")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Scrollbars").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "hidingButton").click()
        self.driver.find_element(By.ID, "hidingButton").click()
        self.driver.find_element(By.ID, "hidingButton").click()
        element = self.driver.find_element(By.ID, "hidingButton")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()


class Test6():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title('переименуй кнопку')
    @allure.feature("жмакни на кнопку")
    @allure.story("стори")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_6(self):
        self.driver.get("http://uitestingplayground.com/home")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Text Input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "newButtonName").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "newButtonName").send_keys("test button ")
        time.sleep(2)
        self.driver.find_element(By.ID, "updatingButton").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "updatingButton").click()
        time.sleep(2)


class Test7():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title("чекбоксы_2")
    @allure.feature("чекбокс")
    @allure.story("нажимаем чекбокс")
    @allure.severity(allure.severity_level.NORMAL)
    def test7(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()


class Test8():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title("скрытый элемент")
    @allure.feature("фича")
    @allure.story("стори")
    @allure.severity(allure.severity_level.NORMAL)
    def test_8(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Dynamic Loading").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Example 1: Element on page that is hidden").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()


class Test9():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title("этот упадет")
    @allure.feature("файл")
    @allure.story("стори")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_9(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "File Download").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "1.txt").click()
        time.sleep(2)
