import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_conditions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Automation, WIN10, En=EN")

webdriver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(webdriver, 15, poll_frequency=1)

webdriver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')

time.sleep(5)