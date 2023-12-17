import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import *

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.join(os.getcwd(), "../downloads")
}
chrome_options.add_experimental_option("prefs", prefs)

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.implicitly_wait(5)

webdriver.get('https://the-internet.herokuapp.com/download')
webdriver.find_element(By.LINK_TEXT, 'abc.txt').click()

time.sleep(3)