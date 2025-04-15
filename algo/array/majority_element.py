# link: https://leetcode.com/problems/majority-element/
# tag: EASY

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List

# O(n)  K(n)
class Solution:
    def majorityElement(nums: List[int]) -> int:
        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        return max(hash_map, key=hash_map.get)


nums = [1, 1, 4, 3, 1, 1, 2, 6, 6, 6]
s = Solution.majorityElement(nums=nums)
print(s)


# class Solution:
#     def majorityElement(nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n//2]
#
#
# nums = [1, 1, 4, 3, 1, 1, 2, 6, 6, 6]
# s = Solution.majorityElement(nums=nums)
# print(s)