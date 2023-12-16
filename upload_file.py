import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import *

chrome_oprions = webdriver.ChromeOptions()

webdriver = webdriver.Chrome()

webdriver.get('https://the-internet.herokuapp.com/upload')

time.sleep(3)

webdriver.find_element(By.ID, 'file-upload').send_keys(f"{os.getcwd()}\\downloads\\abc.txt")

time.sleep(3)