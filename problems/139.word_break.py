from typing import List

"""
    Solution: We use dynamic programming here.
        Defind dp to store matched words in the list 
        Loop through the string and check every char agianst the every word in the list.
        If the last element in dp is true it means the word can be breaked.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        dp = [True] + [False] * len_s
        for index in range(1, len_s + 1):
            for word in wordDict:
                prev_visited_word_index = index - len(word)
                if abs(prev_visited_word_index) <= len_s and dp[prev_visited_word_index] and s[index - len(word):index] == word:
                    dp [index] = True
        return dp[len_s]