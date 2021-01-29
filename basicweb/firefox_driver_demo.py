from selenium import webdriver

class FirefoxDriverDemo():
    def test(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\geckodriver.exe")
        driver.get("http://www.google.com")

ff = FirefoxDriverDemo()
ff.test()

