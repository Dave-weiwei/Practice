from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
time.sleep(3)
a=driver.find_element(By.ID, "a")
b=driver.find_element(By.CLASS_NAME, "btn")
c=driver.find_element(By.CLASS_NAME, "test")
d=driver.find_element(By.NAME, "dog")
add=driver.find_element(By.ID, "add")
sel=Select(driver.find_element(By.ID,"select"))
last_link=driver.find_element(By.LINK_TEXT,"我是超連結，點擊會開啟 Google 網站")


a.click()
print(a.text)
time.sleep(0.5)

b.click()
print(b.text)
time.sleep(0.5)

c.click()
print(c.text)
time.sleep(0.5)

d.click()
print(d.text)
time.sleep(0.5)

add.click()
time.sleep(0.3)
add.click()
time.sleep(0.3)
add.click()
time.sleep(0.3)
time.sleep(0.5)


sel.select_by_index(1)
time.sleep(0.5)
sel.select_by_index(2)
time.sleep(0.5)
sel.select_by_index(3)
time.sleep(0.5)
sel.select_by_index(0)
time.sleep(2)
last_link.click()
time.sleep(2)
#driver.close()