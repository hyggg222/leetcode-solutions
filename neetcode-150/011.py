# Problem: Two Integer Sum II
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150
# Link LeetCode: 

# Memory Constraint: Use O(1) additional space

# Approach: Two Pointer


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1, len(numbers) 
        while (i < j):
            if (numbers[i - 1] + numbers[j - 1] == target):
                break
            elif (numbers[i - 1] + numbers[j - 1] < target):
                i += 1
            else: 
                j -= 1
        return [i, j]