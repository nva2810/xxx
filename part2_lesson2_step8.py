from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Ivan')
    browser.find_element_by_name('lastname').send_keys('Ivan')
    browser.find_element_by_name('email').send_keys('Ivan')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'xxx.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_css_selector('button').click()

finally:
    time.sleep(10)
    browser.quit()
