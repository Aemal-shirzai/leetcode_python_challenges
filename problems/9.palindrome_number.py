class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign = -1 if x < 0 else 1
        return abs(x) == sign * int(str(abs(x))[::-1])