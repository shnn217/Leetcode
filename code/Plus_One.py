"""
66.Plus One [Easy]
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        if len(digits) == 1:
            digits[0] = digits[0] + 1
            if digits[0] == 10:
                ans.append(1)
                ans.append(0)
            else:
                return digits
        
        if len(digits) > 1:
            ans = digits
            digits[-1] = digits[-1] + 1
            for i in sorted(range(len(digits)), reverse = True):
                if digits[i] == 10 and i - 1 >=0:
                    ans[i] = 0
                    ans[i-1] = ans[i-1] + 1
                elif ans[0] == 10:
                    ans[0] = 0
                    ans.insert(0,1)
                
        return ans