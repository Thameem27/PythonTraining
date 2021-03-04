from OddNumCheck import isOddNum
import pytest

@pytest.mark.parametrize(
    "element1,element2,expected",
    [
        (2,False),
        (3,True),
		(5,True),
		(100,True),
    ]
)
def test_exponent_elements(element1):
    assert isOddNum(element) == expected

def test_negative_assert():
    assert isOddNum(4) != False
	
	
@pytest.mark.skip(reason="No need to test this")
def test_zero_exp():
    with pytest.raises(ValueError):
        -1
		

@pytest.mark.skipif(True, reason = "Skipping in Condition")
def test_oddnum_fail():
    assert isOddNum(-1) ==True