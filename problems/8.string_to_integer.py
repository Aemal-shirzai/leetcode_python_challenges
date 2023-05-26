class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        digits = ''
        int_min_val = -2**31
        int_max_val = 2**31 - 1
        
        for index, char in enumerate(s.strip()):
            if index == 0 and char in ['-', '+']:
                sign = -1 if char == '-' else 1
                continue

            if not char.isdigit():
                break

            digits += char

        res = int(digits) * sign if digits else 0
        if not (int_min_val < res < int_max_val):
            res = res < 0 and int_min_val or int_max_val 

        return res
    

# Regex Solution
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        digits = ''
        int_min_val = -2**31
        int_max_val = 2**31 - 1
        
        if s and s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
  
        digit_match = re.match(r'^\d+', s)
        digits = digit_match.group(0) if digit_match else ''

        res = int(digits) * sign if digits else 0
        if not (int_min_val < res < int_max_val):
            res = res < 0 and int_min_val or int_max_val 

        return res
        