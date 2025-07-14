from scr.Index_page import IndexPage
from scr.for_try import use_try
from scr.pic_name import extract_parametrize_id
from scr.json_use import load_test_data
from selenium.webdriver.common.by import By
import pytest

test_click_datas = load_test_data("test_click.json","test_click_update_show")
params = [pytest.param(d["by"], d["target"],d["expected"], id=d["id"]) for d in test_click_datas]
@pytest.mark.parametrize("by, target, expected", params)

def test_default_check(driver, by, target, expected , request):
    page=IndexPage(driver)
    page.open()
    def do_test():
        result=page.click(by, target)
        assert result == expected
    
    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)