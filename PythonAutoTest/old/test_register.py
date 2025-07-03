import scr.register as reg
import pytest
@pytest.mark.parametrize("user, pwd, expected", [
    (68443841, "testtest", "輸入格式錯誤"),
    ("test@test", 35438438438, "輸入格式錯誤"),
    ("@asdasd@gmail.com", "OK123123ok", "輸入格式錯誤"),
    ("asdasd@gmail.com@", "OK123123ok", "輸入格式錯誤"),
    ("asdasdgmail.com", "OK123123ok", "輸入格式錯誤"),
    ("as@as", "OK123123ok", "輸入格式錯誤"),
    ("asdasd@gmail.com", "OKsdfsdfok", "輸入格式錯誤"),
    ("asdasd@gmail.com", "54654654", "輸入格式錯誤"),
    ("asdasd@gmail.com", "5465", "輸入格式錯誤"),
    ("asdasd@gmail.com", "54654654", "輸入格式錯誤")])

def test_reg_user_succes(user, pwd, expected):
    assert reg.register_user(user, pwd) == expected
    
@pytest.mark.parametrize("user, pwd, expected", [
    ("asdasd@gmail.com", "OK123123ok", "註冊成功"),
    ("as@com", "OK123123ok", "註冊成功"),
    ("asdasd@gmail.com", "s123ok", "註冊成功")])   
def test_reg_user_fail(user, pwd, expected):
    assert reg.register_user(user, pwd) == expected