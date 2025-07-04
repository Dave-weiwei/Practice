from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from scr import for_try
import pytest
import time

@pytest.mark.parametrize("input, expected", [
    ("asd", "已提交"),
    ("陳暐翔", "已提交")
])

def test_input_send(driver,input,expected):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    WebDriverWait
    def do_test():
        input_key=driver.find_element(By.ID,"name")
        input_key.send_keys(input)
        btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        btn.click()
        time.sleep(0.3)
        status = driver.find_element(By.ID,"submit-status").get_attribute("textContent")
        assert status == expected
    for_try.use_try(driver,do_test,expected)