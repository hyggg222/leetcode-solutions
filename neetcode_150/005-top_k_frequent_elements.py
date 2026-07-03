# Problem: Top K Frequen Elements
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150
# Link LeetCode: http://leetcode.com/problems/top-k-frequent-elements/

from typing import List

# Easy Approach

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ls = []
        for key, value in freq.items():
            ls.append([value, key])
        ls.sort(reverse = True)
        ans = []
        for i in range(0, min(k, len(ls))):
            ans.append(ls[i][1])
        return ans
        

