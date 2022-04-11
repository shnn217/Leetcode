"""
209.Minimum Size Subarray Sum [Medium]
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        
        total = 0
        ans = float('inf')
        
        while r < len(nums):
            total = total + nums[r]
            if total < target:
                r+=1
            else:
                ans= min(ans,r-l+1)
                total=total-nums[l]-nums[r]
                l+=1
                
        return ans if ans<float('inf') else 0
    
        