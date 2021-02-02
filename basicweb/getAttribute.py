from selenium import webdriver
import time


class GetAttribute():

    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("class")

        print("Value of attribute is " + result)
        time.sleep(1)
        driver.quit()


ff = GetAttribute()
ff.test()