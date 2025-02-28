from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    
 x_element = browser.find_element(By.CSS_SELECTOR, "div.form-group label span.nowrap#input_value")
 x = x_element.text
 y = calc(x)
#Ввести ответ в текстовое поле.
 input = browser.find_element(By.CSS_SELECTOR, "div.form-group input.form-control")
 input.send_keys(y)
#Проскроллить страницу вниз.
 button = browser.find_element(By.TAG_NAME, "button")
 browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#Выбрать checkbox "I'm the robot".
 option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
 option1.click()
#Переключить radiobutton "Robots rule!".
 option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
 option1.click()
#Нажать на кнопку "Submit".
 button.click()

finally:
    
# успеваем скопировать код за 30 секунд
 time.sleep(30)
# закрываем браузер после всех манипуляций
 browser.quit()

# не забываем оставить пустую строку в конце файла