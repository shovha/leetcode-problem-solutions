from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        strlen = len(s)
        if strlen <= 1:
            return s
        noOfShift=0
        for item in shift:
            if(item[0]==0):
                noOfShift += item[1]
            else:
                noOfShift -= item[1]
        s=list(s)
        if(noOfShift>0):
            s.reverse()
            for index in range(noOfShift):
                char=s.pop()
                s = [char]+s
            s.reverse()
        else:
            for index in range(abs(noOfShift)):
                char=s.pop()
                s = [char]+s
        return "".join(s)
solution = Solution()
print(solution.stringShift('abc', [[0, 1], [1, 2]]))  # cab
print(solution.stringShift('abcdefg', [
      [1, 1], [1, 1], [0, 2], [1, 3]]))  # efgabcd
