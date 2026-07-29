# Problem: Longest Repeating Character Replacement
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question?list=neetcode150
# Link LeetCode: 

# Problem Brief: Give a string s and an integer number k. Choose up to k characters of the string and replace to any characters to find the 
# longest substring with only one distinct character.

# Idea: Iterate through every different characters in string s -> With each character, storing all it's indexes into a list
# -> With each list of index of character, find the longest substring with the distinct character is that character.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(list)
        for i in range(len(s)):
            freq[ord(s[i]) - ord("A")].append(i)
        ans = 0
        for i in range(26):
            if (len(freq[i]) == 0):
                continue
            ls = freq[i]
            S, res, l = k, 0, 0
            for r in range(len(ls)):
                if r > 0:
                    S -= (ls[r] - ls[r - 1] - 1)
                while S < 0:
                    S += (ls[l + 1] - ls[l] - 1)
                    l += 1
                curr_len = ls[r] - ls[l] + 1
                total_len = curr_len + min(S, len(s) - curr_len)
                
                ans = max(ans, total_len)
        return ans

# Result: Accept