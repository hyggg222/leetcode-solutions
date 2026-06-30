# Problem: Valid Anagram
# Difficulty: Easy
# Link NeetCode: https://neetcode.io/problems/is-anagram/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/valid-anagram/description/       

# Create a brief of this problem

# check if two strings are anagrams of each other. 
# i dont know what is anagram so let look at the test case
"""
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""
#-> I think the anagram of a string contains the same number of every letters of that string.

# 1 <= s.length, t.lenght <= 5 * 10^4
# consist of lowercase English letters

# Approach 1: Simple
# -> Sort both string and compare -> if they are the same -> return true
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return t == s

# Time complexity: O(n * logn)
# Result: Accepted -> However it only beats 48% of users so I think there is a more optimal solution.

# Approach 2: Dict (char:int)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        ds = {}
        # create a dict of char and it's number of the string s
        for char in s:
            ds[char] = ds.get(char, 0) + 1
        
        # check with string t
        for char in t:
            ds[char] = ds.get(char, 0) - 1
            if (ds[char] < 0):
                return False
        return True
        
# O(n + m + 26)
"""
To optimize the code, we can use a hash map. 
We can leverage this data structure by creating a map that tracks the frequency of each character in string s.
Instead of creating two separate dictionaries and comparing them, we can populate a dictionary for string s first. 
Then, we can iterate through each character of string t. 
For every character we look at in t, we decrement its corresponding value in the hash map by one. 
If we encounter a character whose value in the map is already zero—meaning t has more of this character than s, or the character didn't exist in s at all—we can immediately return False. 
If we successfully finish the loop, we return True.
However, if we only do this, we run into a logical error. 
If s is longer than t, some characters in the hash map will still have leftover positive values. 
Therefore, as an initial check right at the beginning, we must check if the lengths of both strings are equal.
"""

# Insight: Hash map is strong data structure that stores data in unique key-value pairs. Its main advantage is speed,
# as it allows us to look up, insert and delete data in almost O(1) time.