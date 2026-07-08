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
            res = res + str(len(Str)) + "#"
            res = res + Str
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            S = ""
            len_num = 1
            for j in range(i, len(s)):
                if (s[j] == "#"):
                    break
                S = S + s[j]
                len_num += 1
            len_str = int(S)
            res.append(s[i + len_num : i + len_num + len_str])
            i = i + len_num + len_str
        return res

obj = Solution()
ls = ["we","say",":","yes","!@#$%^&*()"]
s = obj.encode(ls)
print(s)
res = obj.decode(s)
print(res)

