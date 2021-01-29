from selenium import webdriver

class ChromeDriverDemo():
    def test(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\chromedriver.exe")
        driver.get("http://google.com")

cc = ChromeDriverDemo()
cc.test()

