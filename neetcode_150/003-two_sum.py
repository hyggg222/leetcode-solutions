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

# Harder Approach: Two pointer
# Create a copy of the array and sort it in ascending order -> initilize two pointers, at the beginning and at the end
# -> Iterate through the array and check if the sum of the two numbers is equal to the target

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = nums
        arr.sort()
        i = 0
        j = len(arr) - 1
        while i < j:
            if (arr[i] + arr[j] == target):
                return [i, j]
            elif   :
    
# More optimal Approach: Using a hash map

import bisect

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(nums):
            if (dct.get(target - nums[i], -1) != -1):
                return [dct[target - nums[i]], i]
            dct[nums[i]] = i

# Result: AC
# Time Complexity: O(n)