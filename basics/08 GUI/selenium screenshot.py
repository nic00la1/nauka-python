from selenium import webdriver # pip install selenium

# pip install webdriver-manager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

import time
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

options = Options()
options.headless = True

service = Service("D:/drivers/msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)

driver.get("https://python.org")
driver.maximize_window()

searchInput = driver.find_element("xpath", '//*[@id="id-search-field"]')
searchInput.send_keys("django")

buttonSubmit = driver.find_element("id", "submit")
buttonSubmit.click()

driver.save_screenshot("python.org.1.png")
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.2.png")

height = driver.execute_script("return document.body.scrollHeight")

driver.set_window_size(1920, height)
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.3.png")

driver.quit()