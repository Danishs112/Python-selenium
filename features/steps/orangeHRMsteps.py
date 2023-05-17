from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given('launch chrome driver')
def launchdriver(context):
    context.driver = webdriver.Chrome("C:\\Users\pc\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")


@when('open orange hrm homepage')
def openOrangeHRMHomepage(context):
    context.driver.get("https://the-internet.herokuapp.com/")


@when('verify that logo is present on the homepage')
def verifyLogo(context):
    webElement = context.driver.find_element(By.XPATH, '//*[contains(text(),‘A/B Testing’)]')
    webElement.click();

@when('I fill (.*) on the search input field')
def enterdata(context,data):
    webElement = context.driver.find_element(By.NAME,'q')
    webElement.send_keys(data)

@when('I fill "search doctors" on the search input field')
def enterdata(context):
    webElement = context.driver.find_element(By.NAME,'q')
    webElement.send_keys("search doctors")
    context.driver.implicitly_wait('1000')
    webElement.send_keys('\ue007')





@then('close browser')
def closeBrowser(context):
    context.driver.close()

