from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class TestFad():

    def test_FAD_search(self):
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "tbFadSearchProviders").click()
        self.driver.find_element(By.ID, "tbFadSearchProviders").send_keys("cardiology")
        # self.driver.find_element(By.ID, "maincontent_0_tbLocationNearSearch").click()
        self.driver.find_element(By.ID, "maincontent_0_tbLocationNearSearch").clear()
        self.driver.find_element(By.ID, "maincontent_0_tbLocationNearSearch").send_keys("19130")
        self.driver.find_element(By.ID, "btnShowProviderResults").click()
        self.driver.find_element(By.ID, "aGenderFilter").click()
        self.driver.find_element(By.NAME, "genderFilter").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fad-form--gender > .js-submitted").click()
        self.driver.find_element(By.ID, "aSpecialtiesFilter").click()
        self.driver.find_element(By.ID, "maincontent_0_rptSpecialtiesFilter_cbSpecialtiesFilter_0").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fad-form--speciality > .js-submitted").click()
        self.driver.find_element(By.ID, "maincontent_0_rptGroups_rptPhysicians_0_imgBadge_0").click()
        # assert self.driver.title.contains == "profile"


