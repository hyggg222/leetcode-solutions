# Problem: Minimum Window Substring
# Difficulty: Hard
# Link NeetCode: https://neetcode.io/problems/minimum-window-with-characters/question?list=neetcode150
# Link LeetCode: 

from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = Counter(t)
        window = defaultdict(int)

        need = len(t_cnt)
        res, res_len = "", float("inf")

        l = 0
        for r in range(len(s)):
            if (window[s[r]] == t_cnt[s[r]] - 1):
                need -= 1
            window[s[r]] += 1
            while (l < r) and (window[s[l]] > t_cnt[s[l]]):
                window[s[l]] -= 1
                l += 1
            if (need == 0) and (r - l + 1 < res_len):
                res_len = r - l + 1
                res = s[l : r + 1]

        return res

func = Solution()
print(func.minWindow("OUZODYXAZV", "XYZ"))

# Time Complex: O(N)
# Result: ACC



        
        
            
