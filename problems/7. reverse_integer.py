class Solution:
    """
        Solution:
            1. Find the sign of the number.
            2. revserse the number by changing to string->reverse->integer
            3. check if the reversed number is > than 2**31 - 1 then return 0 else reversed. 
    """
    def reverse(self, x: int) -> int:
        sign = x < 0 and -1 or 1
        reversed_integer = int(str(abs(x))[::-1]) 
        return 0 if reversed_integer > 2**31 - 1  else sign * reversed_integer