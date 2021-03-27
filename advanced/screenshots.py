from selenium import webdriver
from selenium.webdriver.common.by import By

class Screenshots():

    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        baseURL = "https://letskodeit.teachable.com"
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "/html/body/header/div/div/div/div/ul/li[2]/a").click()
        driver.find_element(By.ID, "user_email").send_keys("test@mail.com")
        driver.find_element(By.ID, "user_password").send_keys("test")
        driver.find_element(By.NAME, "commit").click()
        destinationFileName = "C:\\Users\\malin.nemergut\\Desktop\\seleniumtest.png"

        try:
            driver.save_screenshot(destinationFileName)
            print("screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()
