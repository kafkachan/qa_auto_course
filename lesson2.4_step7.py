from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной h5#price
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[contains(text(), "100")]"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

button = WebDriverWait(browser, 5).until_not(
        EC.element_text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"))
    )