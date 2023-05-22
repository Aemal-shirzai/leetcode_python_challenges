class Solution:
    def isValid(self, s: str) -> bool:
        OPEN = ['(', '{' , '[']
        CLOSE = [')', '}', ']']
        MATCHES = {'(': ')', '{': '}', '[': ']'}
        open_stack = []

        for char in s:
            if char in OPEN:
                open_stack.append(char)
                continue
            
            if not open_stack:
                return False

            if MATCHES.get(open_stack.pop()) != char:
                return False

        return True if not open_stack else False