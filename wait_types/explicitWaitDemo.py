from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo():
    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "http://www.expedia.com"
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)
        driver.find_element(By.ID, "tab-flights-tab").click()
        driver.find_element(By.ID, "flight-origin").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing").send_keys("5/24/2021")
        returnDate = driver.find_element(By.ID, "flight-returning")
        returnDate.clear()
        returnDate.send_keys("5/30/2021")
        driver.find_element(By.ID, "search-button").click()

        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

ff = ExplicitWaitDemo()
ff.test()