# link: https://leetcode.com/problems/squares-of-a-sorted-array/description/
# tag: EASY


# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
# number sorted in non-decreasing order.


from typing import List

class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])




nums = [-4,-1,0,3,10]
print(Solution.sortedSquares(nums))