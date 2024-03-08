def to_roman(arabic_num):
    if not isinstance(arabic_num, int):
        raise TypeError("arabic_num must be an integer")
    if arabic_num <= 0 or arabic_num > 888:
        raise ValueError("NumberOutOfRange")
    roman_numerals = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
  ]

    roman_num = ""
    for symbol, value in roman_numerals:
     while arabic_num >= value:
       roman_num += symbol
       arabic_num -= value

    return roman_num