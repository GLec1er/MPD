# link: https://leetcode.com/problems/two-sum/description/
# tag: EASY

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

nums = [6, 4, 3, 4, 1, 7]
target = 10


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hash_map:
                return [hash_map[diff], i]

            hash_map[num] = i
