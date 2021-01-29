from selenium import webdriver

class IEDriverDemo():
    def test(self):
        driver = webdriver.Ie(executable_path="C:\\Users\\malin.nemergut\\PycharmProjects\\drivers\\IEDriverServer.exe")
        driver.get("http://www.google.com")

ie = IEDriverDemo()
ie.test()
