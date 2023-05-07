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

a = Solution()
print(a.rotateString('abcde', 'abced'))