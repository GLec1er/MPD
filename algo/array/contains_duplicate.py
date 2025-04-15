# link: https://leetcode.com/problems/contains-duplicate/
# tag: EASY

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        return False


nums = [3, 3]
print(Solution.containsDuplicate(nums=nums))

