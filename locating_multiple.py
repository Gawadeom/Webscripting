from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=VHV2G5PX4CDL&sprefix=%2Caps%2C1086&ref=nb_sb_ss_recent_1_0_recent")

elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(f"{len(elems)}items found")
for elem in elems:
    print(elem.text)
#print(elem.get_attribute("outerHTML"))
#print(elem.text)
time.sleep(6)
driver.close()