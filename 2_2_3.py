from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Посчитать сумму заданных чисел
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    num3 =  int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num3))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла