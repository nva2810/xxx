from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.alert.accept()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(10)
    browser.quit()
