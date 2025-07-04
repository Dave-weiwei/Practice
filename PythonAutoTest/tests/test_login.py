from selenium.webdriver.common.by import By
from scr.pic_name import extract_parametrize_id
from scr import for_try
import pytest
import time

def test_input_show(driver):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    time.sleep(1.5)
    def do_test():
        user_input=driver.find_element(By.ID,"login-username")
        user_pwd=driver.find_element(By.ID,"login-password")
        user_input_show=user_input.get_attribute("placeholder")
        user_pwd_show=user_pwd.get_attribute("placeholder")
        assert user_input_show == "帳號"
        assert user_pwd_show == "密碼"
    for_try.use_try(driver,do_test,"input_show")
    time.sleep(0.3)


@pytest.mark.parametrize("username, password, expected", [
    pytest.param("asasdd", "OK88468ok", "登入失敗", id="login_fail"),
    pytest.param("ok88468ok", "OK88468ok", "登入成功", id="login_pass")
])
def test_reg(driver, username, password, expected, request):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    time.sleep(1)

    def do_test():
        user_input = driver.find_element(By.ID, "login-username")
        user_pwd = driver.find_element(By.ID, "login-password")
        sub_btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="登入"]')

        user_input.send_keys(username)
        user_pwd.send_keys(password)
        time.sleep(0.5)
        sub_btn.click()
        show = driver.find_element(By.ID,"login-result").text
        time.sleep(1)
        
        assert show == expected
    pic = extract_parametrize_id(request)
    for_try.use_try(driver, do_test, pic)