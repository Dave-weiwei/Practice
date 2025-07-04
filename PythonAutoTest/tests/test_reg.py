from selenium.webdriver.common.by import By
from scr.pic_name import extract_parametrize_id
from scr import for_try
from scr.db_util import query_user_and_password ,delete_user
import pytest
import time

def test_input_show(driver):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    time.sleep(1.5)
    def do_test():
        user_input=driver.find_element(By.ID,"reg-username")
        user_pwd=driver.find_element(By.ID,"reg-password")
        user_input_show=user_input.get_attribute("placeholder")
        user_pwd_show=user_pwd.get_attribute("placeholder")
        assert user_input_show == "帳號 (至少4碼)"
        assert user_pwd_show == "密碼 (至少6碼含1大寫與數字)"
    for_try.use_try(driver,do_test,"input_show")
    time.sleep(0.3)


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
def test_reg(driver, username, password, expected, request):
    driver.get("file:///D:/PythonAutoTest/web/testweb.html")
    time.sleep(1)

    def do_test():
        user_input = driver.find_element(By.ID, "reg-username")
        user_pwd = driver.find_element(By.ID, "reg-password")
        confirm = driver.find_element(By.ID, "reg-confirm")
        sub_btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="註冊"]')

        user_input.send_keys(username)
        user_pwd.send_keys(password)
        confirm.send_keys(password)
        time.sleep(0.5)
        sub_btn.click()
        time.sleep(1)

        # 驗證欄位是否合法
        valid_u = driver.execute_script("return document.getElementById('reg-username').checkValidity();")
        valid_p = driver.execute_script("return document.getElementById('reg-password').checkValidity();")
        valid_c = driver.execute_script("return document.getElementById('reg-confirm').checkValidity();")
        assert all([valid_u, valid_p, valid_c]) == expected

        result = query_user_and_password(username, password)
        if expected:
            # 驗證是否寫入資料庫
            assert result is not None, "應該成功註冊，但資料庫找不到"
            assert result[0] == username
            assert result[1] == password
        else:
            assert result is None, "預期註冊失敗，但資料竟然寫入資料庫了"

            # 測試後刪除資料
        if result:
            delete_user(username)

    pic = extract_parametrize_id(request)
    for_try.use_try(driver, do_test, pic)