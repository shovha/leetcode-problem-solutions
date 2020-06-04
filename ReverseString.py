from typing import List
import math

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        listLen = len(s)
        for i in range(math.ceil(listLen/2)):
            s[i],s[listLen-1-i] = s[listLen-1-i],s[i]
        return s 

solution = Solution()
print(solution.reverseString([]))