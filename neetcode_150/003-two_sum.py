# Problem: Two Sum
# Difficulty: Easy
# Link NeetCode: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150 
# Link LeetCode: https://leetcode.com/problems/two-sum/description/

# Brief of problem 
# Giving an array and a value
# Return the indicies of two numbers which add up to value
# Only have one solution -> Only need return a pair of indicies for every problem (any order)

from typing import List

# Easy Approach: Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

# Result: AC
# Time Complexity: O(n^2)

