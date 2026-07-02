# Problem: Group Anagrams
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/anagram-groups/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/group-anagrams/

# Brief of problem

# group the anagrams together -> anagrams are strings which have the same frequency of every contained characters

# Easy Approach: Brute Force 

from typing import List

class Solution:
    def check_ana(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        H = {}
        for char in s:
            H[char] = H.get(char, 0) + 1
        for char in t:
            if (char not in H or H[char] == 0):
                return False
            H[char] -= 1
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = [0] * len(strs)
        ans = []
        for i, char in enumerate(strs):
            if (grouped[i] == 0):
                ls = [char]
                for j in range(i + 1, len(strs)):
                    if self.check_ana(strs[j], char):
                        ls.append(strs[j])
                        grouped[j] = 1    
                ans.append(ls)        
        return ans

