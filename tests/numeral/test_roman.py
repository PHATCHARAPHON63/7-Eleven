import pytest
from numeral.roman import to_roman

@pytest.mark.parametrize(
  "arabic_num, roman_num",
  [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (10, "X"),
    (888, "DCCCLXXXVIII"),
    (42, "XLII"),
    (99, "XCIX"),
    (499, "CDXCIX"),
    (888, "DCCCLXXXVIII"),
  ]
)
def test_to_roman_success(arabic_num, roman_num):
  assert to_roman(arabic_num) == roman_num

@pytest.mark.parametrize(
  "arabic_num",
  [
    0,
    -1,
    889,
    1.5,
    "abc",
  ]
)

def test_to_roman_failure(arabic_num):
    with pytest.raises(ValueError):
      to_roman(arabic_num)
