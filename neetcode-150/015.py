# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link NeetCode: https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min = prices[0]
        Profit = 0
        for i in range(1, len(prices)):
            Profit = max(Profit, prices[i] - Min)
            Min = min(Min, prices[i])
        return Profit

# Result: Accepted
# Time Comp: O(n)