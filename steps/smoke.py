from behave import *
import time
from selenium.common.exceptions import NoSuchElementException

@given('teststep')
def login(context):
    context.driver.implicitly_wait(20)

    try:
        context.driver.find_element_by_android_uiautomator('new UiSelector().text("We are for safety!")')
        context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/button2").click()
    except NoSuchElementException:




        context.driver.find_element_by_id("android:id/aerr_wait").click()



    context.driver.implicitly_wait(20)




    context.driver.find_element_by_android_uiautomator('new UiSelector().text("Log in")').click()

    context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/cvUsernameInput").send_keys("7087341574")
    custom_button = context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/customButton")
    custom_button.click()

    context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/etInputText").send_keys("12345678")
    custom_button.click()

    time.sleep(2)

    try:
        context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/ovOtpCode").send_keys('0000')
    except NoSuchElementException:
        print('OK: Otp not called')
    #context.driver.find_element_by_id("kz.homecredit.ibank.debug:id/ovOtpCode").send_keys('0000')



    time.sleep(6)


    print('test ok')