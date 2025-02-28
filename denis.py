import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

def calc(h):
    return str(math.log(abs(12 * math.sin(int(h)))))

 # Нажать на кнопку
 button = browser.find_element(By.CLASS_NAME, "btn")
 button.click()

 # Переключиться на новую вкладку
 new_window = browser.window_handles[1]
 browser.switch_to.window(new_window)

 # Считать значение для переменной x
 robots_radio = browser.find_element(By.ID, "input_value")
 x = robots_radio.text
 # Посчитать математическую функцию от x
 y = calc(x)
 # Ввести ответ в текстовое поле
 input1 = browser.find_element(By.ID, 'answer')
 input1.send_keys(y)
 # Нажать на кнопку "Submit".
 button = browser.find_element(By.CSS_SELECTOR, "button.btn")
 button.click()

finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
 time.sleep(10)
# закрываем браузер после всех манипуляций
 browser.quit()