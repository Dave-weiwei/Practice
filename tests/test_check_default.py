from scr.Index_page import IndexPage
from scr.for_try import use_try
from scr.pic_name import extract_parametrize_id
from scr.json_use import load_test_data
import pytest


default_datas = load_test_data("check_default.json","test_elements")
params = [pytest.param(d["by"], d["target"], id=d["id"]) for d in default_datas]
@pytest.mark.parametrize("by, target", params)

def test_default_check(driver, by, target, request):
    page=IndexPage(driver)
    page.open()
    def do_test():
        result=page.verify_element_exists(by, target)
        assert result == False
    
    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)

    
default_input_datas = load_test_data("check_default.json","test_placeholders_and_texts")
params_input = [pytest.param(d["by"], d["target"],d["expected"], d["source"], id=d["id"]) for d in default_input_datas]
@pytest.mark.parametrize("by, target,expected,source", params_input)

def test_input_default(driver, by, target, expected, source, request):
    page=IndexPage(driver)
    page.open()
    def do_test():
        result=page.verify_input_default(by, target, source)
        assert result == expected
        
    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)