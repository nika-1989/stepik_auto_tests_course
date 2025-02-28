from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    #Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
     #Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    
    #Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    
    #Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла