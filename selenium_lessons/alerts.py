import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_conditions

chrome_options = webdriver.ChromeOptions()

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.implicitly_wait(15)

wait = WebDriverWait(webdriver, 15, poll_frequency=1)

webdriver.get('https://demoqa.com/alerts')
time.sleep(1)
webdriver.find_element(By.ID, 'alertButton').click()
time.sleep(1)
alert = webdriver.switch_to.alert
time.sleep(1)
alert.accept()
time.sleep(1)