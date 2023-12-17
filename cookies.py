import time

from selenium import webdriver
from selenium.webdriver.common.by import *

webdriver = webdriver.Chrome()
webdriver.implicitly_wait(10)

webdriver.get('https://www.demoblaze.com/index.html')

user_cookie = webdriver.get_cookie('user')
print(user_cookie)

webdriver.add_cookie(
    {
        'name': 'Example',
        'value': 'EXAMPLE'
    }
)
print(webdriver.get_cookie('Example'))
time.sleep(1)
before = webdriver.get_cookie('sameSite')
time.sleep(1)
webdriver.delete_cookie('sameSite')
time.sleep(1)
webdriver.add_cookie({
    'name': 'sameSite',
    'value': 'QWERTY'
})
time.sleep(1)
after = webdriver.get_cookie('sameSite')
time.sleep(1)
print(after)






