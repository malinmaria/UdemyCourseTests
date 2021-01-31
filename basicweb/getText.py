from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is " + elementText)
        time.sleep(1)
        driver.quit()


ff = GetText()
ff.test()