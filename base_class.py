from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver, base_url="http://www.uitestpractice.com/"):
        self.base_url = base_url
        self.driver = driver
        self.driver.maximize_window()
        self.timeout = 30

    def open(self):
        url = self.base_url
        self.driver.get(url)

    def click(self, element):
        element.click()

    def waitForVisibility(self, type, element):
        element = self.constructElement(type, element)
        try:
            WebDriverWait(self.driver, 10).until(lambda d: element)
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s")
            self.driver.quit()

    def checkVisibility(self,element):
        status = element.is_displayed()
        assert status is True

    def constructElementPath(self, type, path):
        return self.driver.find_element(type, path)

    def constructElement(self, type, path):
        match type:
            case "id":
                element = self.constructElementPath(By.ID, path)
            case "class":
                element = self.constructElementPath(By.CLASS_NAME, path)
            case "name":
                element = self.constructElementPath(By.NAME, path)
            case "xpath":
                element = self.constructElementPath(By.XPATH, path)
        return element


