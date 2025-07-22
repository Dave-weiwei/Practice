from scr.Index_page import IndexPage
from scr.for_try import use_try
from scr.pic_name import extract_parametrize_id
from scr.db_util import query_user_and_password,delete_user
from scr.json_use import load_test_data
from selenium.webdriver.common.by import By
import pytest

reg_datas = load_test_data("reg_data.json","test_reg")
params_input = [pytest.param(d["user"], d["pwd"],d["confirm"], d["expected"], id=d["id"]) for d in reg_datas]
@pytest.mark.parametrize("user, pwd, confirm, expected", params_input)


def test_reg(driver, user, pwd, confirm, expected,request):
    page=IndexPage(driver)
    page.open()
    
    def do_test():
        delete_user(user)
        reg_result=page.reg(user, pwd, confirm)
        assert reg_result == expected
        result = query_user_and_password(user, pwd)
        if reg_result:
            # 驗證是否寫入資料庫
            assert result is not None, "應該成功註冊，但資料庫找不到"
            assert result[0] == user
            assert result[1] == pwd
        else:
            assert result is None, "預期註冊失敗，但資料竟然寫入資料庫了"

            # 測試後刪除資料
        if result:
            delete_user(user)

    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)