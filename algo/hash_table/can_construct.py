# link: https://leetcode.com/problems/ransom-note/
# tag: EASY



# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
# from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.


from collections import Counter

# class Solution:
#     def canConstruct(ransomNote: str, magazine: str) -> bool:
#         ransom_count = Counter(ransomNote)
#         magazine_count = Counter(magazine)
#
#         for char, count in ransom_count.items():
#             if magazine_count[char] < count:
#                 return False
#
#         return True



class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        if ransom_count & magazine_count == ransom_count:
            return True
        return False



ransomNote = "aa"
magazine = "aab"

print(Solution.canConstruct(ransomNote, magazine))