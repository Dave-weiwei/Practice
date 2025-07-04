from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def test_btn_click():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
    time.sleep(1.5)
    a=driver.find_element(By.ID, "a")
    b=driver.find_element(By.CLASS_NAME, "btn")
    c=driver.find_element(By.CLASS_NAME, "test")
    d=driver.find_element(By.NAME, "dog")
    add=driver.find_element(By.ID, "add")
    a.click()
    a_click=driver.find_element(By.ID,"show").get_attribute("value")
    assert a_click == "A ( id=\"a\" )"
    time.sleep(0.5)
    b.click()
    b_click=driver.find_element(By.ID,"show").get_attribute("value")
    assert b_click == "B ( class=\"btn\" )"
    time.sleep(0.5)
    c.click()
    c_click=driver.find_element(By.ID,"show").get_attribute("value")
    assert c_click == "C ( class=\"test\" )"
    time.sleep(0.5)
    d.click()
    d_click=driver.find_element(By.ID,"show").get_attribute("value")
    assert d_click == "D ( name=\"dog\" )"
    time.sleep(0.5)
    add.click()
    time.sleep(0.5)
    add.click()
    add_click=driver.find_element(By.ID,"show").get_attribute("value")
    assert add_click == "2"
    
    driver.quit()