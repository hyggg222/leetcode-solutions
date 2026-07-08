# Problem: Valid Palindrome
# Difficulty: Easy
# Link NeetCode: https://neetcode.io/problems/is-palindrome/question
# Link LeetCode: https://leetcode.com/problems/word-ladder/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        i, j = 0, len(s) - 1
        while i < j:
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True
        