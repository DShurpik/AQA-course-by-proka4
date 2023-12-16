import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_conditions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1600,1000')

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.implicitly_wait(15)

wait = WebDriverWait(webdriver, 15, poll_frequency=1)

webdriver.get('https://demoqa.com/alerts')
time.sleep(1)
element = webdriver.find_element(By.ID, 'promtButton')
element.click()
time.sleep(1)
alert = wait.until(Exp_conditions.alert_is_present())
time.sleep(1)
alert.send_keys("Hello")
alert.accept()
time.sleep(1)