from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 150);")
    input_1 = browser.find_element_by_id('answer')
    input_1.send_keys(y)
    input_2 = browser.find_element_by_id('robotCheckbox').click()
    input_3 = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(10)
    browser.quit()
