import pytest
import time
from selenium.webdriver.common.by import By
from scr import for_try
#from selenium.webdriver.support.select import Select


@pytest.mark.parametrize("Type, index, expected", [
    (By.CSS_SELECTOR, 'h1[title="我是大標題"]', "大標題"),
    (By.CSS_SELECTOR, 'h2[title="我是次標題"]', "次標題"),
    (By.CLASS_NAME, 'btn', "按鈕點擊"),
])

def test_click(driver, Type, index, expected):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    time.sleep(1)

    def do_test():
        title = driver.find_element(Type, index)
        title.click()
        show= driver.find_element(By.ID,"show").get_attribute("value")
        assert show == expected
    for_try.use_try(driver, do_test,expected)
    time.sleep(0.5)

def test_click_link(driver):
    driver.get("file:///G:/PythonAutoTest/web/testweb.html")
    time.sleep(1)
    def do_test_link():
        link_btn = driver.find_element(By.LINK_TEXT, '我是超連結，點擊會開啟 Google 網站')
        link_btn.click()
        driver.switch_to.window(driver.window_handles[1])
        assert "google.com" in driver.current_url
    for_try.use_try(driver, do_test_link, "like")
    
    time.sleep(0.5)
    