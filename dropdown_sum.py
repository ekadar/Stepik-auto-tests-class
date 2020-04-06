from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    x_element = browser.find_element_by_css_selector("#num1")
    y_element = browser.find_element_by_css_selector("#num2")
    summ = int(x_element.text) + int(y_element.text)
    summ = str(summ)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summ)

    button = browser.find_element_by_css_selector("[type=submit]")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()