# Problem: Container With Most Water
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/max-water-container/question      
# Link LeetCode: 

# Problem Brief: Amount of water a container can store equal to
# min_height(two bars) * distance(two bars)

# Easy Approach: Look at every pairs of bars - Brute Force

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                ans = max(ans, (j - i) * min(heights[i], heights[j]))
        return ans

# Time Complexity: O(n^2)

# 