# Problem: Encode and Decode Strings
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/string-encode-and-decode/question

# Problem's Brief: Create two function
# 1. Encode: List of strings -> one string
# 2. Decode: that string -> Original list of strings

# Important point: strings can contain any letter or syntax
# Idea: Use the length of string and store it before the string position in the decoded string

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for Str in strs:
            res = res + str(len(Str))
            res = res + Str
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i == len(s):
            l = int(s[i])
            res.append(s[i + 1 : i + l])
            i = i + 1 + l
        return res

obj = Solution()

