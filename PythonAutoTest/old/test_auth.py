import pytest
import scr.auth as auth
import json

with open("json/login_test_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


@pytest.mark.parametrize("username, password, expected", data["cases"])
def test_auth(username, password,expected):
    assert auth.login_check(username,password) == expected
