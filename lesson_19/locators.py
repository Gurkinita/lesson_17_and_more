from selenium.webdriver.common.by import By

class Locators:
    # Elements_Page
    BUTTONS_BUTTON = (By.CSS_SELECTOR, ".show #item-4 > .text")
    CLICKME_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button")
    CLICKME_RESULT = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p")
    RADIO_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[3]/span")
    YES_BUTTON = (By.CSS_SELECTOR, ".custom-control:nth-child(2) > .custom-control-label")
    YES_TEXT = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p/span")

    # widgets_Page
    SELECTDATE_FIELD = (By.ID, "datePickerMonthYearInput")
    MONTHSELECT_BUTTON = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DECEMBER_BUTTON = (By.XPATH, "//option[. = 'December']")
    YEARSELECT_BUTTON = (
    By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select')
    YEAR_1916_BUTTON = (
    By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[17]')
    DATESELECT_BUTTON = (By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[1]')
    DATEANDTIME_BUTTON = (By.XPATH, '//*[@id="dateAndTimePickerInput"]')
    TIMESELECT_BUTTON = (By.XPATH, '//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[53]')

    # Text_box page
    USERNAME_FIELD = (By.ID, "userName")
    USEREMAIL_FIELD = (By.ID, "userEmail")
    CURRENTADDRESS_FIELD = (By.ID, "currentAddress")
    PERMANENTADDRESS_FIELD = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_DIV = (By.XPATH, "//*[@id='output']/div")


