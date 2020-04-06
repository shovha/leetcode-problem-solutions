from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Approach 1: My solution
        sortedStrs = collections.defaultdict(list)
        for index in range(len(strs)):
            sortedStr = "".join(sorted(strs[index]))
            sortedStrs[sortedStr].append(strs[index])
        return list(sortedStrs.values()) 


        # Approach 2: Categorize by Count
        # Intuition
        # Two strings are anagrams if and only if their character counts (respective number of occurrences of each
        # character) are the same.
        
        # Algorithm
        # We can transform each string \text{s}s into a character count, \text{count}count, consisting of 26 
        # non-negative integers representing the number of \text{a}a's, \text{b}b's, \text{c}c's, etc. 
        # We use these counts as the basis for our hash map.

        # In python, the representation will be a tuple of the counts. For example, abbccc will be 
        # (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.

        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))                              