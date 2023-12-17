import time

from selenium import webdriver
from selenium.webdriver.common.by import *

webdriver = webdriver.Chrome()
webdriver.implicitly_wait(3)
webdriver.maximize_window()

webdriver.get('https://www.demoblaze.com/index.html')
time.sleep(2)
webdriver.find_element(By.ID, 'login2').click()
time.sleep(2)

user_name_field = webdriver.find_element(By.ID, 'loginusername')
user_name_field.send_keys('USER')
time.sleep(2)
# Проверка того что текст действительно ввелся в поле используя аттрибут value

value_user_field = user_name_field.get_attribute('value')
print(value_user_field)

user_password_field = webdriver.find_element(By.ID, 'loginpassword')
user_password_field.send_keys('PASSWORD')

time.sleep(2)

value_password_field = user_password_field.get_attribute('value')
print(value_password_field)

time.sleep(2)

field_after_cleaning = user_password_field.clear()
print(field_after_cleaning)

time.sleep(2)

user_password_field.send_keys('PASSWORD2')
print(user_password_field.get_attribute('value'))

time.sleep(2)

webdriver.quit()