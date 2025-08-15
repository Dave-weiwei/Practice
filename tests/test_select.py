from scr.Index_page import IndexPage
from scr.for_try import use_try
from scr.pic_name import extract_parametrize_id
from scr.json_use import load_test_data
import pytest

test_sel_datas = load_test_data("test_select.json","test_select_options")
params = [pytest.param(d["sel_item"], d["expected"], id=d["id"]) for d in test_sel_datas]
@pytest.mark.parametrize("sel_item, expected", params)

def test_default_check(driver, sel_item, expected , request):
    page=IndexPage(driver,)
    page.open()
    def do_test():
        sel_text, show_val=page.select(sel_item)
        assert sel_text == expected
        assert show_val == expected
    
    pic = extract_parametrize_id(request)
    use_try(driver, do_test, pic)