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
# Can use the idea of 2sum: Sort and iterate through every value -> Find other two
# value that equals to (Target (0) - First Value).

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if (nums[i] > 0):
                break
            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            cur_Tar = -(nums[i])
            j, z = i + 1, len(nums) - 1
            while j < z:
                cur_Sum = nums[j] + nums[z]
                if (cur_Sum == cur_Tar):
                    ans.append((nums[i], nums[j], nums[z]))
                    j += 1
                    z -= 1
                    while nums[j] == nums[j - 1] and j < z:
                        j += 1
                elif (cur_Sum < cur_Tar):
                    j += 1
                else:
                    z -= 1
        
        return ans

# Time Complexity: O(n^2)
# Space Complexity: O(1) 

# Result: Accepted