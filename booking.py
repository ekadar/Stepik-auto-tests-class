from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import os
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button_price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button_book = browser.find_element_by_css_selector("#book")
    button_book.click()
    button_solve = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_solve)
    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button_solve.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
