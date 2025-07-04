import scr.id_check as id_c
import json
import pytest

with open("json/id_check_data.json",encoding="utf=8") as file:
    ids=json.load(file)

@pytest.mark.parametrize("id", ids["ID_fail"])
def test_id_check_fail(id):
    assert id_c.is_valid_tw_id(id) == False
    
@pytest.mark.parametrize("id", ids["ID_pass"])
def test_id_check_pass(id):
    assert id_c.is_valid_tw_id(id) == True
    
def test_id_check_trigger_exception():
    class Dummy:
        pass
    assert id_c.is_valid_tw_id(Dummy()) == False