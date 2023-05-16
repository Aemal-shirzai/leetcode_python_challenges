class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** x
    
obj = Solution()
print(obj.myPow(2, 4))