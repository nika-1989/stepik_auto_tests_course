from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
 button = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
 browser.find_element(By.ID, "book").click() #нажимаем на кнопку
#Проскроллить страницу вниз.
 button = browser.find_element(By.ID, "solve")
 browser.execute_script("return arguments[0].scrollIntoView(true);", button)
 x_element = browser.find_element(By.CSS_SELECTOR, "div.form-group label span.nowrap#input_value")
 x = x_element.text
 y = calc(x)
# Ввести ответ в текстовое поле.
 input = browser.find_element(By.ID, "answer")
 input.send_keys(y)
 button.click()


finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла