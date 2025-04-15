# link: https://leetcode.com/problems/valid-anagram/
# tag: EASY


from collections import Counter

class Solution:
    def isAnagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"

print(Solution.isAnagram(s, t))