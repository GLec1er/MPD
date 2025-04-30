# link: https://leetcode.com/problems/sort-colors/description/
# tag: MEDIUM

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.


from typing import List


class Solution:
    def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        return nums




nums = [2,0,2,1,1,0]
#0 0 2 1 1 2
print(Solution.sortColors(nums))
