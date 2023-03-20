from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url="http://github.com"

driver.get(url)

search_input = driver.find_element("/html/body/div[1]/div[6]/main/div/div[1]/div/form/input[1]")
time.sleep(1)
search_input.send_keys("python")
time.sleep(2)
search_input.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.page_source
print(result)


driver.close()