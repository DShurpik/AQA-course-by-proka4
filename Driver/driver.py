import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#.add_argument('--headless')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--window-size=1200,800')
chrome_options.add_argument('--disable-cache')


driver = webdriver.Chrome(options=chrome_options)
#driver.set_window_size(1200, 800)
driver.implicitly_wait(3)




driver.get('https://www.demoblaze.com/index.html')
time.sleep(2)
url = driver.current_url
window_handle = driver.current_window_handle
title = driver.title
print(url, window_handle, title)

driver.close()
driver.quit()
