from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    browser.find_element(By.NAME, "firstname").send_keys("Вероника")
    browser.find_element(By.NAME, "lastname").send_keys("Сиделева")
    browser.find_element(By.NAME, "email").send_keys("lkjhg@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path) #загружаем файл
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click() #нажимаем на кнопку
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла