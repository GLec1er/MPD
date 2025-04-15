# link: https://leetcode.com/problems/valid-parentheses/description/
# tag: EASY



# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.



class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            else:
                if not stack or bracket_map[bracket] != stack.pop():
                    return False
        if stack:
            return False
        return True


s = "([])"
print(Solution.isValid(s))