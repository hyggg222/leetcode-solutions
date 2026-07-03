# Problem: Top K Frequen Elements
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150
# Link LeetCode: http://leetcode.com/problems/top-k-frequent-elements/

from typing import List

# Easy Approach

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ls = []
        for key, value in freq.items():
            ls.append([value, key])
        ls.sort(reverse = True)
        ans = []
        for i in range(0, min(k, len(ls))):
            ans.append(ls[i][1])
        return ans

# Time Complexity: O(nlogn)

# More optimal approach: Using a Min Heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if (len(heap) > k):
                heapq.heappop(heap)
                
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

# Time Complexity: O(N * LogK)

# More Optimal Sol: Distribution Count
# Optimize the way we count the top largest -> Solution (Watch later)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
