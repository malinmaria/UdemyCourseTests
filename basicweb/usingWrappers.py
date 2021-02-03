from selenium import webdriver
from utilities.handyWrappers import HandyWrappers
import time


class UsingWrappers():

    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textField1 = hw.getElement("name")
        textField1.send_keys("test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name]", locatorType="xpath")
        textField2.clear()


ff = UsingWrappers()
ff.test()
