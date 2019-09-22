#-*-coding: utf-8 -*-

from appium import webdriver
# from appium.common import exceptions
from selenium.common import exceptions

# set the search keyword
KEYWORD = u"coco"

# setup the desired_capablity
cap = {
    # "deviceName": "127.0.0.1:62001", # Nox mock app
    "deviceName": "127.0.0.1:7555", # NetEasy mock app
    "platformName": "Android",
    "appPackage": "com.douguo.recipe",
    "appActivity": ".MainActivity",
    "noReset": True,
    "platformVersion": "6.0.1",
    "newCommandTimeout": "6000", # set expire time
}

# TODO: connect
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=cap)
driver.wait_activity(".HomeActivity", 50)
# TODO: close the adv window
try:
    driver.find_element_by_id("com.douguo.recipe:id/close").click()
except exceptions.NoSuchElementException:
    pass
# TODO: Get the device size
WIDTH = driver.get_window_size()["width"]
HEIGHT = driver.get_window_size()["height"]

# search the keyword
driver.find_element_by_id("com.douguo.recipe:id/search_container").click()

search_page = driver.find_element_by_id("com.douguo.recipe:id/search_text")
search_page.send_keys(KEYWORD)
# click search button
driver.find_element_by_id("com.douguo.recipe:id/search_button").click()
driver.wait_activity(".RecipeResultListActivity", 30)

# click recipe tab
driver.find_element_by_xpath("//android.widget.TextView[@text='菜谱']").click()

# swipe the window
# If End imageView display, stop swipe
end = False
while not end:
    driver.swipe(WIDTH * 0.5, HEIGHT * 0.8, WIDTH * 0.5, HEIGHT * 0.2, duration=250)
    # use exception to control swipe
    try:
        end = driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.douguo.recipe:id/list_ending']/android.widget.ImageView[1]")\
            .is_displayed()
    except exceptions.NoSuchElementException:
        pass

