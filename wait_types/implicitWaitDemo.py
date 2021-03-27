from selenium import webdriver
from selenium.webdriver.common.by import By

class ImplicitWaitDemo():
    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "https://letskodeit.teachable.com"
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[href='log_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

ff = ImplicitWaitDemo()
ff.test()