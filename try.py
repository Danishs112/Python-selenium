import time
from telnetlib import EC
from tkinter import Button
import os
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchFrameException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from base_class import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from pyautogui import moveTo

driver = webdriver.Chrome(service=Service("C:\\Users\pc\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"))

# def LoginPage():
#     driver.find_element(By.ID, 'username').send_keys("tom-smith")
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


# def Checkboxes():
#     page.waitForVisibility("xpath", '//*[text()="Checkboxes"]')
#     webElement = page.constructElement("xpath", '//*[text()="Checkboxes"]')
#     page.click(webElement)
#     WebElement = page.constructElement("xpath", '//*[@id="checkboxes"]//input[1]')
#     assert WebElement.is_selected() == False
#     webElement1 = page.constructElement("xpath", '//*[@id="checkboxes"]//input[2]')
#     assert webElement1.is_selected() == True
#
#
# Checkboxes()


# def contextMenu():
#     page.waitForVisibility("xpath", '//*[text()="Context Menu"]')
#     webElement = page.constructElement("xpath", '//*[text()="Context Menu"]')
#     page.click(webElement)
#     page.waitForVisibility("xpath", '//*[text()="Context Menu"]')
#     webElement1 = driver.find_element(By.ID, "hot-spot")
#     WebDriverWait(driver, 10).until(lambda d: webElement1)
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "hot-spot"))
#         )
#     finally:
#         driver.quit()
#     action = ActionChains(driver)
#     action.context_click(webElement1).perform()
#     print("danish")
#
#
# contextMenu()

#
# def DynamicControls():
#     page.waitForVisibility("xpath", '//*[text()="Dynamic Controls"]')
#     webElement = page.constructElement("xpath", '//*[text()="Dynamic Controls"]')
#     page.click(webElement)
#     page.waitForVisibility("id", 'checkbox')
#     webElement = page.constructElement("xpath", '//*[@type="checkbox"]')
#     page.click(webElement)
#
#     assert webElement.is_selected() == True
#     button = page.constructElement("xpath",'//*[text()="Remove"]')
#     button.click()
#     driver.implicitly_wait(2000)
#     WebDriverWait(driver, 10).until(lambda d: driver.find_element("id", "message"))
#     buttonElement = page.constructElement("xpath", '//*[text()="Add"]')
#     buttonElement.click()
#     insertion_text = page.constructElement("xpath",'//*[text()="It\'s back!"]')
#     WebDriverWait(driver, 10).until(lambda d: insertion_text)
#     assert insertion_text.text == "It's back!"
#
#     enable_button = page.constructElement("xpath", '//*[text()="Enable"]')
#     enable_button.click()
#     disable_button = page.constructElement("xpath",'//*[text()="It\'s enabled!"]')
#     WebDriverWait(driver,10).until(lambda d:disable_button)
#
#     input_field = page.constructElement("xpath", '//*[@id="input-example"]//input')
#     input_field.send_keys("danish")
#     assert input_field.get_attribute('value') == "danish"
#
# DynamicControls()


# def DropDown():
#     page.waitForVisibility("xpath", '//*[text()="Dropdown"]')
#     webElement = page.constructElement("xpath", '//*[text()="Dropdown"]')
#     page.click(webElement)
#     select = Select(page.constructElement("id", "dropdown"))
#     select.select_by_visible_text("Option 1")
#     time.sleep(0.8)
#     select.select_by_index(2)
#     time.sleep(0.4)
#     select.select_by_value("1")
#     time.sleep(0.5)
#
#
# DropDown()


# def dynamicLoading1():
#     page.waitForVisibility("xpath", '//*[text()="Dynamic Loading"]')
#     webElement = page.constructElement("xpath", '//*[text()="Dynamic Loading"]')
#     page.click(webElement)
#     element1 = page.constructElement("xpath", '//*[@class="example"]//a[1]')
#     page.click(element1)
#     WebDriverWait(driver, 10).until(
#         lambda d: page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
#     page.checkVisibility(page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
#     element1 = page.constructElement("xpath", '//*[text()="Start"]')
#     page.click(element1)
#     try:
#         WebDriverWait(driver, 10).until(
#             lambda d: page.constructElement("xpath", '//*[text()="Hello World!"]'))
#     except:
#         print("error")
#     time.sleep(5)
#     element = driver.find_element(By.XPATH, '//*[text()="Hello World!"]')
#     page.checkVisibility(element)
#
#
# dynamicLoading1()

# def dynamicLoading2():
#     page.waitForVisibility("xpath", '//*[text()="Dynamic Loading"]')
#     webElement = page.constructElement("xpath", '//*[text()="Dynamic Loading"]')
#     page.click(webElement)
#     element1 = page.constructElement("xpath", '//*[@class="example"]//a[2]')
#     page.click(element1)
#     WebDriverWait(driver, 10).until(
#         lambda d: page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
#     page.checkVisibility(page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
#     element1 = page.constructElement("xpath", '//*[text()="Start"]')
#     page.click(element1)
#     try:
#         WebDriverWait(driver, 10).until(
#             lambda d: page.constructElement("xpath", '//*[text()="Hello World!"]'))
#     except:
#         print("error")
#     time.sleep(5)
#     element = driver.find_element(By.XPATH, '//*[text()="Hello World!"]')
#     page.checkVisibility(element)
#
#
# dynamicLoading2()


# def entryAd():
#     page.waitForVisibility("xpath", '//*[text()="Entry Ad"]')
#     webElement = page.constructElement("xpath", '//*[text()="Entry Ad"]')
#     page.click(webElement)
#     time.sleep(10)
#
#     modal_element = driver.find_element(By.CLASS_NAME, 'modal')
#     title_element = modal_element.find_element(By.CLASS_NAME, 'modal-title')
#     body_element = modal_element.find_element(By.CLASS_NAME, 'modal-body')
#     close_button = modal_element.find_element(By.XPATH, './/div[@class="modal-footer"]//p')
#     title_text = title_element.text
#     body_text = body_element.text
#     close_button.click()
#     status = modal_element.is_displayed()
#     assert status is False
#
# entryAd()


def exitIntent():
    page.waitForVisibility("xpath", '//*[text()="Exit Intent"]')
    webElement = page.constructElement("xpath", '//*[text()="Exit Intent"]')
    page.click(webElement)
    moveTo(600, 0)
    modal_element = driver.find_element(By.CLASS_NAME,'modal')
    status = modal_element.is_displayed()
    assert status is True

# exitIntent()


def fileDownload():
    page.waitForVisibility("xpath", '//*[text()="File Download"]')
    webElement = page.constructElement("xpath", '//*[text()="File Download"]')
    page.click(webElement)
    webElements = driver.find_elements(By.TAG_NAME,"a")
    for element in webElements:
        print(element.text)
    ele = driver.find_element(By.XPATH,'//*[text()="index.html"]')
    ele.click()

# fileDownload()


def fileUpload():
    page.waitForVisibility("xpath", '//*[text()="File Upload"]')
    webElement = page.constructElement("xpath", '//*[text()="File Upload"]')
    page.click(webElement)
    file_upload_button = driver.find_element(By.ID,"file-upload")
    file_upload_button.send_keys("E:\pythonProject\pythonProject\dummy.jpg")
    upload_button = page.constructElement("id","file-submit")
    upload_button.click()
    WebDriverWait(driver, 10).until(lambda d: page.constructElement("id","uploaded-files").is_displayed())
    time.sleep(10)


# fileUpload()

