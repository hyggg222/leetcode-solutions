# Problem: Longest Consecutive Sequence 
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/

# First approach: DSU + Hash Table
# ext[exist, parent, link (if not parent), size (if parent)]

import collections
from typing import List

class Solution:
    def FindPar(self, x: int) -> int:
        if (self.ext[x][1] != -1):
            return x
        self.ext[x][2] = self.FindPar(self.ext[x][2])
        return self.ext[x][2]
    def Uni(self, x: int, y: int):
        x = self.FindPar(x)
        y = self.FindPar(y)
        if (self.ext[x][3] < self.ext[y][3]):
            x, y = y, x
        self.ext[y][1] = -1
        self.ext[y][2] = x
        self.ext[x][3] += self.ext[y][3]
        self.ans = max(self.ans, self.ext[x][3])
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        self.ext = collections.defaultdict(lambda: [-1] * 4)
        self.ans = 1
        for num in nums:
            if (self.ext[num][0] != -1):
                continue
            self.ext[num][0] = 1
            self.ext[num][1] = 1
            self.ext[num][3] = 1
            if self.ext[num - 1][0] != -1:
                self.Uni(num, num - 1)
            if self.ext[num + 1][0] != -1:
                self.Uni(num, num + 1)
        return self.ans
            
obj = Solution()
nums=[2,20,4,10,3,4,5]
print(obj.longestConsecutive(nums))

# Optimal Approach: Using a hash set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            if (num - 1) in num_set: 
                continue
            cur_num = num
            cur_streak = 1
            while (cur_num + 1) in num_set:
                cur_streak += 1
                cur_num += 1
            ans = max(ans, cur_streak)
        
        return ans
    
# Another Solution: Using hash table
# There are just three ways possible to add a number to form a sequence: head, in the middle (only one), tail
# Therefore we just have to save the updated value of these positions

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:         
        dct = collections.defaultdict(int)
        ans = 0

        for num in nums:
            if not dct[num]:
                dct[num] = dct[num - 1] + dct[num + 1] + 1
                dct[num - dct[num - 1]] = dct[num]
                dct[num + dct[num + 1]] = dct[num]
                ans = max(ans, dct[num])

        return ans  


            
        
