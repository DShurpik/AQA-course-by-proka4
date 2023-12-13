from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get('https://www.demoblaze.com/index.html')

url = driver.current_url
window_handle = driver.current_window_handle
title = driver.title

assert url == 'https://www.demoblaze.com/index.html'
assert title == 'STORE'



print(url, window_handle, title)


driver.close()
driver.quit()