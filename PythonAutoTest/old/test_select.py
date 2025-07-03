from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def test_select_all():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
    time.sleep(1.5)
    sel=Select(driver.find_element(By.ID,"select"))
    sel.select_by_index(1)
    sel_set = sel.first_selected_option.text
    sel_show = driver.find_element(By.ID,"show").get_attribute("value")
    assert sel_set == "GKPen"
    assert sel_show == "GKPen"
    time.sleep(0.5)
    sel.select_by_index(2)
    sel_set = sel.first_selected_option.text
    sel_show = driver.find_element(By.ID,"show").get_attribute("value")
    assert sel_set == "OK"
    assert sel_show == "OK"
    time.sleep(0.5)
    sel.select_by_index(3)
    sel_set = sel.first_selected_option.text
    sel_show = driver.find_element(By.ID,"show").get_attribute("value")
    assert sel_set == "Hello"
    assert sel_show == "Hello"
    time.sleep(0.5)
    sel.select_by_index(0)
    sel_set = sel.first_selected_option.text
    sel_show = driver.find_element(By.ID,"show").get_attribute("value")
    assert sel_set == "OXXO"
    assert sel_show == "OXXO"
    time.sleep(2)
    driver.quit()