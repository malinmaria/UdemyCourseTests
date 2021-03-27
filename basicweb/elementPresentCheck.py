from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handyWrappers import HandyWrappers


class ElementPresentCheck():

    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()
