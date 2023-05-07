"""
    Solution:
    Keep shifting the leftmost to the right most unless the string become the initial string
    If the string became the initial string: It is not equal False
    If the string is equal to goal: It is equal True
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def rotate_string(target):
            res = target[1:] + target[0]
            if res == goal:
                return True
            if res == s:
                return False
            
            return rotate_string(res)
        
        return rotate_string(s)