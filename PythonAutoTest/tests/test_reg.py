from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from scr.pic_name import extract_parametrize_id
from scr import for_try
import pytest
import time

#fail
@pytest.mark.parametrize("username, password, expected", [
    pytest.param("asd", "OK88468ok", False, id="fail_short_username"),
    pytest.param("asdasd", "ok88468ok", False, id="fail_no_uppercase"),
    pytest.param("asdasd", "OKasdasdok", False, id="fail_no_number"),
    pytest.param("asdasd", "846846848", False, id="fail_no_uppercase_only_numbers"),
    pytest.param("asdasd", "Ok345", False, id="fail_too_short_password"),
    pytest.param("asde", "OK88468ok", True, id="pass_case1"),
    pytest.param("asdasd", "O848468", True, id="pass_case2"),
    pytest.param("asdasd", "OK8846", True, id="pass_case3"),
])


def test_input_show(driver):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    WebDriverWait
    def do_test():
        user_input=driver.find_element(By.ID,"reg-username")
        user_pwd=driver.find_element(By.ID,"reg-password")
        user_input_show=user_input.get_attribute("placeholder")
        user_pwd_show=user_pwd.get_attribute("placeholder")
        assert user_input_show == "帳號 (至少4碼)"
        assert user_pwd_show == "密碼 (至少6碼含1大寫與數字)"
    for_try.use_try(driver,do_test,"input_show")
    time.sleep(0.3)

def test_reg(driver, username, password, expected, request):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    WebDriverWait
    def do_test():
        user_input=driver.find_element(By.ID,"reg-username")
        user_pwd=driver.find_element(By.ID,"reg-password")
        sub_btn=driver.find_element(By.CSS_SELECTOR,'input[type="submit"]')
        user_input.send_keys(username)
        user_pwd.send_keys(password)
        sub_btn.click()
        valid = driver.execute_script("return document.getElementById('reg-username').checkValidity();")
        assert valid is expected
    
    pic = extract_parametrize_id(request)    
    for_try.use_try(driver,do_test, pic)