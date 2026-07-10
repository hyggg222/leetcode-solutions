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

ans.add((nums[i], nums[j], nums[z]))

# Time Complexity: O(n^3)
# Result: Time Limit Exceeded

# Insight: Optimize the last loop - Check if there is a value = -(nums[i] + nums[j])
# that has the indicies > j -> Can use Hash Map

# Another Approach: Hash Map