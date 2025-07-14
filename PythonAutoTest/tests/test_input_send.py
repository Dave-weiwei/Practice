from scr.Index_page import IndexPage
from scr.for_try import use_try
from scr.pic_name import extract_parametrize_id
from scr.json_use import load_test_data
from selenium.webdriver.common.by import By
import pytest

test_send_datas = load_test_data("send_input.json","test_submit_name")
params = [pytest.param(d["name_text"], d["expected"], id=d["id"]) for d in test_send_datas]
@pytest.mark.parametrize("name_text, expected", params)

def test_input_send(driver,name_text,expected, request):
    page=IndexPage(driver)
    page.open()
    
    def do_test():
        result = page.input_send(name_text)
        assert result == expected
    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)