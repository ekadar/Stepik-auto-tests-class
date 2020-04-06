from selenium import webdriver
import math
import os
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_css_selector("button")
    button.click()
    time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_css_selector("#input_value")
    x_element = x_element.text
    y = calc(x_element)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()