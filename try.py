import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


from base_class import BasePage
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from pyautogui import moveTo
from selenium.webdriver.support import expected_conditions as EC

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


def AddRemove():
    page.waitForVisibility("xpath", '//*[text()="Add/Remove Elements"]')
    webElement = page.constructElement("xpath", '//*[text()="Add/Remove Elements"]')
    page.click(webElement)
    driver.implicitly_wait(20)
    page.waitForVisibility("xpath", '//*[text()="Add/Remove Elements"]')
    webElement1 = page.constructElement("xpath", '//*[text()="Add Element"]')
    page.click(webElement1)
    page.waitForVisibility("xpath", '//*[@id="elements"]//button')
    webElement1 = page.constructElement("xpath", '//*[@id="elements"]//button')
    webElement1.click()
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
#
#
# Checkboxes()


def contextMenu():
    page.waitForVisibility("xpath", '//*[text()="Context Menu"]')
    webElement = page.constructElement("xpath", '//*[text()="Context Menu"]')
    page.click(webElement)
    page.waitForVisibility("xpath", '//*[text()="Context Menu"]')
    webElement1 = driver.find_element(By.ID, "hot-spot")
    WebDriverWait(driver, 10).until(lambda d: webElement1)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hot-spot"))
        )
    finally:
        driver.quit()
    action = ActionChains(driver)
    action.context_click(webElement1).perform()
    print("danish")
#
#
# contextMenu()

#
def DynamicControls():
    page.waitForVisibility("xpath", '//*[text()="Dynamic Controls"]')
    webElement = page.constructElement("xpath", '//*[text()="Dynamic Controls"]')
    page.click(webElement)
    page.waitForVisibility("id", 'checkbox')
    webElement = page.constructElement("xpath", '//*[@type="checkbox"]')
    page.click(webElement)

    assert webElement.is_selected() == True
    button = page.constructElement("xpath",'//*[text()="Remove"]')
    button.click()
    driver.implicitly_wait(2000)
    WebDriverWait(driver, 10).until(lambda d: driver.find_element("id", "message"))
    buttonElement = page.constructElement("xpath", '//*[text()="Add"]')
    buttonElement.click()
    insertion_text = page.constructElement("xpath",'//*[text()="It\'s back!"]')
    WebDriverWait(driver, 10).until(lambda d: insertion_text)
    assert insertion_text.text == "It's back!"

    enable_button = page.constructElement("xpath", '//*[text()="Enable"]')
    enable_button.click()
    disable_button = page.constructElement("xpath",'//*[text()="It\'s enabled!"]')
    WebDriverWait(driver,10).until(lambda d:disable_button)

    input_field = page.constructElement("xpath", '//*[@id="input-example"]//input')
    input_field.send_keys("danish")
    assert input_field.get_attribute('value') == "danish"
#
# DynamicControls()


def DropDown():
    page.waitForVisibility("xpath", '//*[text()="Dropdown"]')
    webElement = page.constructElement("xpath", '//*[text()="Dropdown"]')
    page.click(webElement)
    select = Select(page.constructElement("id", "dropdown"))
    select.select_by_visible_text("Option 1")
    time.sleep(0.8)
    select.select_by_index(2)
    time.sleep(0.4)
    select.select_by_value("1")
    time.sleep(0.5)
#
#
# DropDown()


def dynamicLoading1():
    page.waitForVisibility("xpath", '//*[text()="Dynamic Loading"]')
    webElement = page.constructElement("xpath", '//*[text()="Dynamic Loading"]')
    page.click(webElement)
    element1 = page.constructElement("xpath", '//*[@class="example"]//a[1]')
    page.click(element1)
    WebDriverWait(driver, 10).until(
        lambda d: page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
    page.checkVisibility(page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
    element1 = page.constructElement("xpath", '//*[text()="Start"]')
    page.click(element1)
    try:
        WebDriverWait(driver, 10).until(
            lambda d: page.constructElement("xpath", '//*[text()="Hello World!"]'))
    except:
        print("error")
    time.sleep(5)
    element = driver.find_element(By.XPATH, '//*[text()="Hello World!"]')
    page.checkVisibility(element)
#
#
# dynamicLoading1()

def dynamicLoading2():
    page.waitForVisibility("xpath", '//*[text()="Dynamic Loading"]')
    webElement = page.constructElement("xpath", '//*[text()="Dynamic Loading"]')
    page.click(webElement)
    element1 = page.constructElement("xpath", '//*[@class="example"]//a[2]')
    page.click(element1)
    WebDriverWait(driver, 10).until(
        lambda d: page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
    page.checkVisibility(page.constructElement("xpath", '//*[text()="Dynamically Loaded Page Elements"]'))
    element1 = page.constructElement("xpath", '//*[text()="Start"]')
    page.click(element1)
    try:
        WebDriverWait(driver, 10).until(
            lambda d: page.constructElement("xpath", '//*[text()="Hello World!"]'))
    except:
        print("error")
    time.sleep(5)
    element = driver.find_element(By.XPATH, '//*[text()="Hello World!"]')
    page.checkVisibility(element)

# dynamicLoading2()


def entryAd():
    page.waitForVisibility("xpath", '//*[text()="Entry Ad"]')
    webElement = page.constructElement("xpath", '//*[text()="Entry Ad"]')
    page.click(webElement)
    time.sleep(10)

    modal_element = driver.find_element(By.CLASS_NAME, 'modal')
    title_element = modal_element.find_element(By.CLASS_NAME, 'modal-title')
    body_element = modal_element.find_element(By.CLASS_NAME, 'modal-body')
    close_button = modal_element.find_element(By.XPATH, './/div[@class="modal-footer"]//p')
    title_text = title_element.text
    body_text = body_element.text
    close_button.click()
    status = modal_element.is_displayed()
    assert status is False
#
# entryAd()


def exitIntent():
    page.waitForVisibility("xpath", '//*[text()="Exit Intent"]')
    webElement = page.constructElement("xpath", '//*[text()="Exit Intent"]')
    page.click(webElement)
    moveTo(600, 0)
    modal_element = driver.find_element(By.CLASS_NAME, 'modal')
    status = modal_element.is_displayed()
    assert status is True


# exitIntent()


def fileDownload():
    page.waitForVisibility("xpath", '//*[text()="File Download"]')
    webElement = page.constructElement("xpath", '//*[text()="File Download"]')
    page.click(webElement)
    webElements = driver.find_elements(By.TAG_NAME, "a")
    for element in webElements:
        print(element.text)
    ele = driver.find_element(By.XPATH, '//*[text()="index.html"]')
    ele.click()


# fileDownload()


def fileUpload():
    page.waitForVisibility("xpath", '//*[text()="File Upload"]')
    webElement = page.constructElement("xpath", '//*[text()="File Upload"]')
    page.click(webElement)
    file_upload_button = driver.find_element(By.ID, "file-upload")
    file_upload_button.send_keys("E:\pythonProject\pythonProject\dummy.jpg")
    upload_button = page.constructElement("id", "file-submit")
    upload_button.click()
    WebDriverWait(driver, 10).until(lambda d: page.constructElement("id", "uploaded-files").is_displayed())


# fileUpload()


def floatingMenu():
    page.waitForVisibility("xpath", '//*[text()="Floating Menu"]')
    webElement = page.constructElement("xpath", '//*[text()="Floating Menu"]')
    page.click(webElement)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight")


# floatingMenu()


def forgotPassword():
    page.waitForVisibility("xpath", '//*[text()="Forgot Password"]')
    webElement = page.constructElement("xpath", '//*[text()="Forgot Password"]')
    page.click(webElement)
    input_field = page.constructElement("id", "email")
    input_field.send_keys("danish.soma@alphaitsystems.com")
    time.sleep(3)
    retrieve_button = driver.find_element(By.XPATH, "//*[text()='Retrieve password']")
    action = ActionChains(driver)
    action.click(retrieve_button).perform()
    time.sleep(5)
    ele = driver.find_element(By.TAG_NAME, "h1")
    assert ele.is_displayed()


# forgotPassword()


def nestedFrames():
    page.waitForVisibility("xpath", '//*[text()="Frames"]')
    webElement = page.constructElement("xpath", '//*[text()="Frames"]')
    page.click(webElement)
    element = driver.find_element(By.LINK_TEXT, 'Nested Frames')
    element.click()
    iframe = driver.find_element(By.NAME, "frame-top")
    driver.switch_to.frame(iframe)
    left_iframe = driver.find_element(By.NAME, "frame-left")
    driver.switch_to.frame(left_iframe)
    test = driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2)')
    assert test.text == "LEFT"

    driver.switch_to.default_content()

    iframe = driver.find_element(By.NAME, "frame-top")
    driver.switch_to.frame(iframe)
    left_iframe = driver.find_element(By.NAME, "frame-middle")
    driver.switch_to.frame(left_iframe)
    test = driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2)')
    assert test.text == "MIDDLE"

    driver.switch_to.default_content()

    iframe = driver.find_element(By.NAME, "frame-top")
    driver.switch_to.frame(iframe)
    left_iframe = driver.find_element(By.NAME, "frame-right")
    driver.switch_to.frame(left_iframe)
    test = driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2)')
    assert test.text == "RIGHT"

    driver.switch_to.default_content()

    iframe = driver.find_element(By.NAME, "frame-bottom")
    driver.switch_to.frame(iframe)
    test = driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2)')
    assert test.text == "BOTTOM"


# nestedFrames()


def iframe():
    pass


# iframe()


def geolocation():
    page.waitForVisibility("xpath", '//*[text()="Geolocation"]')
    webElement = page.constructElement("xpath", '//*[text()="Geolocation"]')
    page.click(webElement)
    button = driver.find_element(By.CSS_SELECTOR, "#content button")
    button.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="map-link"]//a')))
    link_text = driver.find_element(By.XPATH, '//*[@id="map-link"]//a')
    link_text.click()
    current_url = driver.current_url
    assert "maps" in current_url


# geolocation()


def horizontal_slider():
    page.waitForVisibility("xpath", '//*[text()="Horizontal Slider"]')
    webElement = page.constructElement("xpath", '//*[text()="Horizontal Slider"]')
    page.click(webElement)

    slider = driver.find_element(By.TAG_NAME, 'input')
    for index in range(0, 8):
        slider.send_keys(Keys.ARROW_RIGHT)


# horizontal_slider()


def hover():
    page.waitForVisibility("xpath", '//*[text()="Hovers"]')
    webElement = page.constructElement("xpath", '//*[text()="Hovers"]')
    page.click(webElement)
    time.sleep(10)

    ist_image = driver.find_element(By.CSS_SELECTOR, '[alt="User Avatar"]:nth-child(1)')
    action = ActionChains(driver)
    action.move_to_element(ist_image).perform()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="View profile"]')))
    view_profile = driver.find_element(By.XPATH, '//*[text()="View profile"]')
    view_profile.click()
    current_url = driver.current_url
    assert "users/1" in current_url

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    not_found_element = driver.find_element(By.TAG_NAME, 'h1')
    not_found_element.is_displayed()
    time.sleep(10)


# hover()

def scroll_to_bottom():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)


def infiniteScroll():
    page.waitForVisibility("xpath", '//*[text()="Infinite Scroll"]')
    webElement = page.constructElement("xpath", '//*[text()="Infinite Scroll"]')
    page.click(webElement)
    count = 10
    for _ in range(0, count):
        scroll_to_bottom()


# infiniteScroll()


def inputs():
    page.waitForVisibility("xpath", '//*[text()="Inputs"]')
    webElement = page.constructElement("xpath", '//*[text()="Inputs"]')
    page.click(webElement)
    input_field = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    input_field.send_keys(12324)
    time.sleep(5)


# inputs()

def jqueryUIElementsBackToJQueryUI():
    page.waitForVisibility("xpath", '//*[text()="JQuery UI Menus"]')
    webElement = page.constructElement("xpath", '//*[text()="JQuery UI Menus"]')
    page.click(webElement)

    enabled_button = page.constructElement("xpath", '//ul[@id="menu"]//li[2]')
    enabled_button.click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Back to JQuery UI"]')))
    back_to_ui_button = page.constructElement("xpath", '//*[text()="Back to JQuery UI"]')
    back_to_ui_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content')))
    menu_button = driver.find_element(By.LINK_TEXT, 'Menu')
    menu_button.click()
    content = driver.find_element(By.CLASS_NAME, 'example')
    assert content.is_displayed()


# jqueryUIElementsBackToJQueryUI()


def jqueryUIElementDownloads():
    page.waitForVisibility("xpath", '//*[text()="JQuery UI Menus"]')
    webElement = page.constructElement("xpath", '//*[text()="JQuery UI Menus"]')
    page.click(webElement)

    enabled_button = page.constructElement("xpath", '//ul[@id="menu"]//li[2]')
    enabled_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Downloads"]')))
    back_to_ui_button = page.constructElement("xpath", '//*[text()="Downloads"]')
    back_to_ui_button.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CSV')))
    csv_button = driver.find_element(By.LINK_TEXT, 'CSV')
    csv_button.click()

    time.sleep(10)


# jqueryUIElementDownloads()


def javascriptAlert():
    page.waitForVisibility("xpath", '//*[text()="JavaScript Alerts"]')
    webElement = page.constructElement("xpath", '//*[text()="JavaScript Alerts"]')
    page.click(webElement)

    alert_button = driver.find_element(By.XPATH, '//*[text()="Click for JS Alert"]')
    alert_button.click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    time.sleep(2)
    text = alert.text
    print(text)
    alert.accept()


# javascriptAlert()


def javascriptConfirmAlert():
    page.waitForVisibility("xpath", '//*[text()="JavaScript Alerts"]')
    webElement = page.constructElement("xpath", '//*[text()="JavaScript Alerts"]')
    page.click(webElement)

    confirm_button = driver.find_element(By.XPATH, '//*[text()="Click for JS Confirm"]')
    confirm_button.click()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    text = alert.text
    print(text)

    alert.dismiss()
    output = driver.find_element(By.ID, 'result')
    assert 'Cancel' in output.text
    time.sleep(10)


# javascriptConfirmAlert()

def javascriptPromptAlert():
    word = "danish soma"
    page.waitForVisibility("xpath", '//*[text()="JavaScript Alerts"]')
    webElement = page.constructElement("xpath", '//*[text()="JavaScript Alerts"]')
    page.click(webElement)

    prompt_button = driver.find_element(By.XPATH, '//*[text()="Click for JS Prompt"]')
    prompt_button.click()

    alert = Alert(driver)

    alert.send_keys(word)

    alert.accept()

    output = driver.find_element(By.ID, 'result')
    assert word in output.text


# javascriptPromptAlert()


def KeyPresses():
    page.waitForVisibility("xpath", '//*[text()="Key Presses"]')
    webElement = page.constructElement("xpath", '//*[text()="Key Presses"]')
    page.click(webElement)
    key_presses = driver.find_element(By.ID, 'target')
    key_presses.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'result')))


# KeyPresses()


def newWindowHandle():
    page.waitForVisibility("xpath", '//*[text()="Multiple Windows"]')
    webElement = page.constructElement("xpath", '//*[text()="Multiple Windows"]')
    page.click(webElement)

    original_window_handle = driver.current_window_handle
    print(len(driver.window_handles))
    assert len(driver.window_handles) == 1

    click_here = driver.find_element(By.LINK_TEXT,'Click Here')

    click_here.click()

    WebDriverWait(driver,10).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window_handle:
            driver.switch_to.window(window_handle)
            break

    assert driver.title == "New Window"



# newWindowHandle()

def notification_messages():
    page.waitForVisibility("xpath", '//*[text()="Notification Messages"]')
    webElement = page.constructElement("xpath", '//*[text()="Notification Messages"]')
    page.click(webElement)

    element = driver.find_element(By.XPATH,'//div[@id="flash-messages"]//div[@id="flash"]')

    assert element.is_displayed()

# notification_messages()


def redirection_link():
    page.waitForVisibility("xpath", '//*[text()="Redirect Link"]')
    webElement = page.constructElement("xpath", '//*[text()="Redirect Link"]')
    page.click(webElement)
    here_button = driver.find_element(By.ID,'redirect')
    here_button.click()
    status_button = driver.find_element(By.XPATH,'//*[@class="example"]//ul//li//a')
    redirect_url = status_button.get_attribute("href")
    driver.get(redirect_url)
    assert redirect_url == driver.current_url


# redirection_link()


def broken_images():
    page.waitForVisibility("xpath", '//*[text()="Broken Images"]')
    webElement = page.constructElement("xpath", '//*[text()="Broken Images"]')
    page.click(webElement)

    images = driver.find_elements(By.TAG_NAME,'img')
    for image in images:
        src = image.get_attribute("src")
        response = requests.head(src)
        if response.status_code != 200:
            print(src)



#broken_images()


def drag_and_drop():
    # page.waitForVisibility("xpath", '//*[text()="Drag and Drop"]')
    # webElement = page.constructElement("xpath", '//*[text()="Drag and Drop"]')
    # page.click(webElement)
    # time.sleep(5)
    source_element = driver.find_element(By.ID,'draggable')
    target_element = driver.find_element(By.ID,'droppable')
    #
    actions = ActionChains(driver)
    #
    # actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

    actions.drag_and_drop(source_element, target_element).perform()


# drag_and_drop()


def double_click():
    button = driver.find_element(By.CLASS_NAME,'btn-default')
    actions = ActionChains(driver)
    actions.double_click(button).perform()
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    text = alert.text
    print(text)



# double_click()


def iframe():
    word ="danish"
    iframe = driver.find_element(By.NAME,'iframe_a')
    driver.switch_to.frame(iframe)
    input_field = driver.find_element(By.ID,'name')
    input_field.send_keys(word)

    text = input_field.get_attribute("value")
    assert word == text
    time.sleep(10)

# iframe()

def new_tab():
    button = driver.find_element(By.ID,'Button')
    button.click()
    original_tab =  driver.current_window_handle
    for tab in driver.window_handles:
        if tab != original_tab:
            driver.switch_to.window(tab)
            break
    iframe()




# new_tab()

def new_window():
    button = driver.find_element(By.CSS_SELECTOR,'.container.Compli button')
    button.click()

    original_window = driver.current_window_handle

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            break

    play_button = driver.find_element(By.CLASS_NAME,'ytp-play-button')
    play_button.click()
    time.sleep(3)
    play_button.click()
    time.sleep(10)

new_window()


