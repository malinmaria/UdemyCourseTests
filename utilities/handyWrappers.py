from selenium import webdriver
from selenium.webdriver.common.by import By


class HandyWrappers():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        else:
            print("locator type is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver .find_element(byType, locator)
            print("element found")
        except:
            print("element not found")
        return element
