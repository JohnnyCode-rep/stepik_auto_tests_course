from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока цена не станет равной 100$
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element(By.ID, 'book') #После того, как цена снизилась до 100, кликаем по кнопке
button.click()
# Появляется капча для роботов. Работаем с ней как раньше:

import math

input_value = browser.find_element(By.ID, 'input_value') # считываем х
x = input_value.text

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

y = calc(x)

input = browser.find_element(By.ID, 'answer')
input.send_keys(y)

button = browser.find_element(By.XPATH, '//button[@type="submit"]')
button.click()