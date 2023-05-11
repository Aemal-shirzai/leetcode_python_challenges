class Solution():
    def find_fist_recurring_char(self, string: str):
        visited = []
        for char in string:
            if char in visited:
                return char
            else:
                visited.append(char)
        return None
    

# Test Case
obj = Solution()
print(obj.find_fist_recurring_char('ABC'))