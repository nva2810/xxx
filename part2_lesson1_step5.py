from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input_1 = browser.find_element_by_class_name('form-control')
    input_1.send_keys(y)
    input_2 = browser.find_element_by_css_selector('[type="checkbox"]')
    input_2.click()
    input_3 = browser.find_element_by_id('robotsRule')
    input_3.click()
    button = browser.find_element_by_css_selector('button')
    button.click()

finally:
    # выход из браузера
    time.sleep(10)
    browser.quit()
