# link: https://leetcode.com/problems/group-anagrams/
# tag: MEDIUM

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other


from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution.groupAnagrams(strs))
