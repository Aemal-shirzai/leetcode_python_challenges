class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        current_substring = ''
        for char in s:
            if char in current_substring:
                current_substring = current_substring[current_substring.index(char)+1:]
            
            current_substring += char
            substrings.append(len(current_substring))

        return substrings and max(substrings) or 0