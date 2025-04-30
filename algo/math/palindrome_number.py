# link: https://leetcode.com/problems/palindrome-number/description/
# tag: EASY


# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]




x = -121
y = 121
print(Solution.isPalindrome(x))
print(Solution.isPalindrome(y))