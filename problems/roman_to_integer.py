ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
ORDERS = list(ROMAN_NUMERALS.keys())

class Solution:
    def romanToInt(self, s: str):
        result = index = 0
        while index < len(s):
            if index < len(s)-1 and ORDERS.index(s[index]) < ORDERS.index(s[index + 1]):
                result += ROMAN_NUMERALS.get(s[index + 1]) - ROMAN_NUMERALS.get(s[index])
                index += 1
            else:
                result += ROMAN_NUMERALS.get(s[index])
            index += 1
        return result