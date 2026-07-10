# Problem: 3Sum
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/three-integer-sum/question?list=neetcode150
# Link LeetCode: 

# Problem Brief
# Input: an integer array
# Output: List of triplets of values whose sum = 0, with distinct indices
# Output and triplets in any order 

from typing import List

# First approach: Brute Force

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for z in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[z] == 0):
                        ans.add((nums[i], nums[j], nums[z]))
        return list(ans)
        

# Time Complexity: O(n^3)
# Result: Time Limit Exceeded

# Insight: Optimize the last loop - Check if there is a value = -(nums[i] + nums[j])
# that has the indicies > j -> Can use Hash Map to store the latest index of a value

# Another Approach: Hash Map

import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        dct = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            dct[num] = idx
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                lst_vl = -(nums[i] + nums[j])
                if (dct[lst_vl] > j):
                    ans.add((nums[i], nums[j], lst_vl))
        return list(ans)
    
# Time Complexity: O(n^2)
# Memory Usage: Addditional Space = O(2n)
# Result: Accepted

# Insight: We should minimize the memory usage -> get risk of data structures