#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if isinstance(roman_string, str) and not roman_string == None:
        numerals = {"M": 1000, "D": 500, "C": 100, 
                "L": 50, "X": 10, "V": 5, "I": 1}
        for i, c in enumerate(roman_string):
            num += numerals[c]
            if i < len(roman_string) - 1:
                if numerals[c] < numerals[roman_string[i + 1]]:
                    num -= numerals[c] * 2
    return num
