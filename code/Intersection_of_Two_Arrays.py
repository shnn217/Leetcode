"""
349.Intersection of Two Arrays [Easy]
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1={}
        hash2={}
        ans=[]
        for num in nums1:
            hash1[num] = 1
        
        for num in nums2:
            hash2[num] = 1
            
        for key in hash1:
            if key in hash2:
                ans.append(key)
                
        return ans