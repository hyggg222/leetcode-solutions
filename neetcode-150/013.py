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

# Optimal Approach: Greedy + Two Pointers
# Value Fomula, with i < j are the bars: ans = max of (j - i) * min(heights[i], heights[j])
# Start with i at the beginning and j at the end -> maximum the (j - i) -> From now on this value only decreases so min(heights[i], heights[j]) 
# makes the value increase.
# How to find the max(min(height[i], height[j])) -> Move the indicie that has smaller value

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i, j = 0, len(heights) - 1
        while i < j:
            ans = max(ans, (j - i) * min(heights[i], heights[j]))
            if (heights[i] < heights[j]):
                i += 1
            else:
                j -= 1
        return ans

# Time Comp: O(n)
# Insight: Greedy is so hard