from scr.Index_page import IndexPage
from scr.for_try import use_try
from scr.pic_name import extract_parametrize_id
from scr.json_use import load_test_data
from selenium.webdriver.common.by import By
import pytest

datas = load_test_data("login_test.json","test_login")
params = [pytest.param(d["user"], d["pwd"], d["expected"], id=d["id"]) for d in datas]
@pytest.mark.parametrize("user, pwd, expected", params)

def test_reg(driver, user, pwd, expected,request):
    page=IndexPage(driver)
    page.open()
    
    def do_test():
        result=page.login(user, pwd)
        assert result == expected
        
        
    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)