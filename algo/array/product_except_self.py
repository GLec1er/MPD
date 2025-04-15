# link: https://leetcode.com/problems/product-of-array-except-self/
# tag: MEDIUM

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # Слева - направо
        left = 1
        for i in range(len(nums)):
            result[i] *= left
            left *= nums[i]

        # Справа - налево
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result


nums = [2, 3, 3, 3]
print(Solution.productExceptSelf(nums))