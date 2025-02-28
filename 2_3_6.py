from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click() #нажимаем на кнопку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) #переключаем вкладку
    x_element = browser.find_element(By.CSS_SELECTOR, "div.form-group label span.nowrap#input_value")
    x = x_element.text ##На новой странице решить капчу для роботов, чтобы получить число с ответом
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input = browser.find_element(By.CSS_SELECTOR, "div.form-group input.form-control")
    input.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click() #нажимаем на кнопку

finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла