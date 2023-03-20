from selenium import webdriver
import time
driver = webdriver.Chrome()

url = 'http://github.com'

driver.get(url)

time.sleep(2)
driver.maximize_window()
# driver.save_screenshot("github.com-homepage.png")

url = "https://github.com/arkeolog-yazilimci"
driver.get(url)

print(driver.title)

if "kartderin" in driver.title:
    driver.save_screenshot("github-kartalderin.png")

time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)

driver.close()