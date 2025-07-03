import scr.bmi as bmi
import pytest

@pytest.mark.parametrize("h, w, expected", [
    (170, 53, "體重過輕"),
    (170, 53.465, "正常"),
    (170, 60, "正常"),
    (170, 72, "過重"),
    (170, 80, "輕度肥胖"),
    (170, 95, "中度肥胖"),
    (170, 105, "重度肥胖"),
    (170, 101.15, "重度肥胖")])
def test_bmi_pass(h,w,expected):
    assert bmi.bmi_category(h,w)==expected

@pytest.mark.parametrize("h, w, expected", [
    (0, 53, "請輸入正確身高體重"),
    (170, 0, "請輸入正確身高體重"),
    (-25, 60, "請輸入正確身高體重"),
    (170, -99, "請輸入正確身高體重"),
    (170, "qwdw", "輸入錯誤"),
    ("ABC", -99, "輸入錯誤")])
def test_bmi_fault(h,w,expected):
    assert bmi.bmi_category(h,w)==expected