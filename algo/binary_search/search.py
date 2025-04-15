# link: https://leetcode.com/problems/binary-search/
# tag: EASY


# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
# search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.


from typing import List


class Solution:
    def search(nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            quess = nums[mid]

            if quess == target:
                return mid

            elif quess > target:
                high = mid - 1

            else:
                low = mid + 1

        return -1


nums = [-1,0,3,5,9,12]
target = 2

print(Solution.search(nums, target))
