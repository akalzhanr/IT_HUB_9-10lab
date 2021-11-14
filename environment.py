import os
from appium import webdriver


def before_scenario(context, scenario):
    desired_cap = {"deviceName": "Nexus6P", "platformName": "Android", "app": os.path.abspath(
        os.path.abspath
        ("D:/IT_HUB_Homework/white_test.apk")
    ), "appPackage": "kz.homecredit.ibank.debug", "appActivity": (
        "cz.bsc.mb.activities.prelogin.SplashScreenActivity"
    ), "newCommandTimeout": 2000}

    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


def after_scenario(context, scenario):
    context.driver.quit()
