"""
3.Longest Substring Without Repeating Characters [Medium]
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        res, start_idx = 0, 0
        for i in range(len(s)):
            if s[i] in seen and start_idx <= seen[s[i]]:
                start_idx = seen[s[i]] + 1
            else:
                res = max(res, i - start_idx + 1)
            seen[s[i]] = i
        return res
            