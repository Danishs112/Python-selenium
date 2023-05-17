from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base_class import BasePage

driver = webdriver.Chrome(service=Service("C:\\Users\pc\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"))

# def LoginPage():
#     driver.find_element(By.ID, 'username').send_keys("tomsmith")
#     driver.find_element(By.ID, 'password').send_keys("SuperSecretPassword!")
#     driver.find_element(By.XPATH, '//*[text()=" Login"]').click()
#     get_url = driver.current_url
#     try:
#         WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH, '//*[text()=" Logout"]'))
#     except TimeoutException:
#         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s")
#         driver.quit()
#
#     driver.find_element(By.XPATH, '//*[text()=" Logout"]').click()
#     get_url = driver.current_url
#     print(get_url)
#
#
# def click(element):
#     element.click()
#
#
# def waitForVisibility(type, element):
#     element = constructElement(type, element)
#     try:
#         WebDriverWait(driver, 10).until(lambda d: element)
#     except TimeoutException:
#         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s")
#         driver.quit()
#
#
# def checkVisibility(element):
#     status = element.is_displayed()
#     assert status is True
#
#
# def constructElementPath(type, path):
#     return driver.find_element(type, path)
#
#
# def constructElement(type, path):
#     match type:
#         case "id":
#             element = constructElementPath(By.ID, path)
#         case "class":
#             element = constructElementPath(By.CLASS_NAME, path)
#         case "name":
#             element = constructElementPath(By.NAME, path)
#         case "xpath":
#             element = constructElementPath(By.XPATH, path)
#     return element
page = BasePage(driver)
page.open()


def ABTesting():
    page.waitForVisibility("xpath", '//*[text()="A/B Testing"]')
    webElement = page.constructElement("xpath", '//*[text()="A/B Testing"]')
    page.click(webElement)
    page.waitForVisibility("xpath", '//*[text()="A/B Test Control"]')
    webElement1 = page.constructElement("xpath", '//*[text()="A/B Test Control"]')
    assert webElement1.text == "A/B Test Control"
    page.checkVisibility(webElement1)


# ABTesting()


# def AddRemove():
#     page.waitForVisibility("xpath", '//*[text()="Add/Remove Elements"]')
#     webElement = page.constructElement("xpath", '//*[text()="Add/Remove Elements"]')
#     page.click(webElement)
#     driver.implicitly_wait(20)
#     page.waitForVisibility("xpath", '//*[text()="Add/Remove Elements"]')
#     webElement1 = page.constructElement("xpath", '//*[text()="Add Element"]')
#     page.click(webElement1)
#     page.waitForVisibility("xpath", '//*[@id="elements"]//button')
#     webElement1 = page.constructElement("xpath", '//*[@id="elements"]//button')
#     webElement1.click()
#
#
# AddRemove()


def Checkboxes():
    page.waitForVisibility("xpath", '//*[text()="Checkboxes"]')
    webElement = page.constructElement("xpath", '//*[text()="Checkboxes"]')
    page.click(webElement)
    WebElement = page.constructElement("xpath", '//*[@id="checkboxes"]//input[1]')
    assert WebElement.is_selected() == False
    webElement1 = page.constructElement("xpath", '//*[@id="checkboxes"]//input[2]')
    assert webElement1.is_selected() == True


Checkboxes()
