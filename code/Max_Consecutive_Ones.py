"""
485.Max Consecutive Ones [Easy]
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_max = 0
        for item in nums:
            if item == 1:
                count += 1
            else:
                if count>count_max:
                    count_max = count
                count = 0
        if count>count_max:
            count_max = count
            
        
        return count_max