import pytest
import scr.grade as grade

def test_grade():
    assert grade.grade(100) == "A"
    assert grade.grade(0) == "F"
    assert grade.grade(95.6) == "A"
    assert grade.grade(83) == "B"
    assert grade.grade(79) == "C"
    assert grade.grade(62.3) == "D"
    assert grade.grade(59) == "F"
    with pytest.raises(ValueError,match="分數必須在 0~100 之間"):
        grade.grade(103)
    with pytest.raises(ValueError,match="分數必須在 0~100 之間"):
        grade.grade(-24)
    with pytest.raises(ValueError,match="分數必須是數字"):
        grade.grade("asd")