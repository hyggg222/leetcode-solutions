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
        for i, Str in enumerate(strs):
            if (grouped[i] == 0):
                ls = [Str]
                for j in range(i + 1, len(strs)):
                    if self.check_ana(strs[j], Str):
                        ls.append(strs[j])
                        grouped[j] = 1    
                ans.append(ls)        
        return ans

# Time complexity: O(n^2 + k)

# Better Approach
# Sort all the strings n the array (ana become the same string) -> Sort the array (ana are next to each others) 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        for i, Str in enumerate(strs):
            arr.append([sorted(Str), i])
        arr.sort()
        ans = []
        ls = [strs[arr[0][1]]]
        for i in range(1, len(strs)):
            if (arr[i][0] == arr[i-1][0]):
                ls.append(strs[arr[i][1]])
            else:
                ans.append(ls)
                ls = [strs[arr[i][1]]]
        ans.append(ls)
        return ans
# Time complexity: O(nklogk)

# Another approach: Hash Table using dict
# Using a hash map: <key>: tuple of dict of frequency of character - <value>: list of strings

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for Str in strs:
            dt = {}
            for char in Str:
                dt[char] = dt.get(char, 0) + 1
            key = tuple(sorted(dt.items()))
            if key not in dct:
                dct[key] = []
            dct[key].append(Str)
        return list(dct.values())


# Time complexity: O(nk)
# Slightly More Optimal Approach:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for Str in strs:
            ls = [0] * 26
            for char in Str:
                ls[ord(char) - ord('a')] += 1
            hashVal = tuple(ls)
            ans[hashVal] = ans.get(hashVal, []).append(s)
        return ans
                


        