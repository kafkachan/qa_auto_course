from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Vasyan')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Kudaybergenov')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('Vasyan.K@gmail.com')
 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt') 
    input4 = browser.find_element(By.CSS_SELECTOR, '#file')
    input4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()