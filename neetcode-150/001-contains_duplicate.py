# Problem: Contains Duplicate
# Difficulty: Easy
# Link NeetCode: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/contains-duplicate/description/

# Problem Brief
# Check if there is at least one duplicate in an array
# If there is return True else return False

from typing import List

# Approach 1 - Brute Force
# Use a list to store every existing value

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ls = []
        for num in nums:
            if num not in ls:
                ls.append(num)
            else:
                return True
        return False

# Results: 70/79 Test Cases -> Time Limit Error
# I need a more optimal solution

# Approach 2 - Use a data structure that can automatically check duplicate
# Ill use a set for simple. Set is a data structure that only store distinct value
# So if I convert an array into set -> Duplicate values will be decreased to 1 -> array's len change
# so if the orginal length of an array is diff from its set version' len -> it contains duplicate -> return true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# Result: Accepted 79/79
# Insight: I should think about using a set when solving a problem relating to the number of values