"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# Naive but 95% efficient solution. But donot follow instruction "without using the division operation"

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]* len(nums)
        if nums.count(0) > 1:
            return ans
        mlt = 1
        mlo = 1
        for i in nums:
            if i != 0:
                mlo *= i
            mlt *= i
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = mlo
            else:
                nums[i] = mlt // nums[i]
        return nums
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
            