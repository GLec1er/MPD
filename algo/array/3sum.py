# link: https://leetcode.com/problems/3sum/
# tag: MEDIUM


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        nums.sort()  # Сортируем массив
        print(nums)
        result = []

        for i in range(len(nums) - 2):  # Проходим по массиву
            if i > 0 and nums[i] == nums[i - 1]:  # Пропускаем дублирующие элементы
                continue
            left, right = i + 1, len(nums) - 1  # Два указателя
            print(left, right)

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:  # Сумма слишком маленькая
                    left += 1
                elif total > 0:  # Сумма слишком большая
                    right -= 1
                else:  # Сумма равна 0
                    result.append([nums[i], nums[left], nums[right]])

                    # Пропускаем одинаковые элементы слева
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Пропускаем одинаковые элементы справа
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
print(Solution.threeSum(nums))