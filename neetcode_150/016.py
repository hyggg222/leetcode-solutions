# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Optimal Approach:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        se = set()
        while j < len(s):
            if s[j] in se:
                while (s[j] in se):
                    se.remove(s[i])
                    i += 1
            se.add(s[j])
            # print(f'Valid {i} {j}')
            # print(' '.join(num for num in se))
            ans = max(ans, j - i + 1)
            j += 1
        return ans

# Time Comp: O(n)

from collections import defaultdict

# Slightly more optimal solution: Instead of removing characters 1by1, jump directly to the correct position by saving that last index of each character
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        dct = defaultdict(lambda: -1)
        while j < len(s):
            if dct[s[j]] != -1:
                i = max(i, dct[s[j]] + 1)
            ans = max(ans, j - i + 1)
            dct[s[j]] = j
            j += 1
        return ans

# Time Comp: O(n)
# Result: Accepted d