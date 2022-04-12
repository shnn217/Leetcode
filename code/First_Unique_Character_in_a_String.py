"""
387.First Unique Character in a String [Easy]
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        smap={}
        for c in s:
            if c not in smap:
                smap[c]=1
            else:
                smap[c]+=1
        
        for v in smap:
            if smap[v] == 1:
                return s.index(v)
        
        return -1
                
        