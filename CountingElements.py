from typing import List
import collections

class Solution:
    def countElements(self, arr: List[int]) -> int:
        itemArrCount=collections.defaultdict(int)
        for item in arr:
            itemArrCount[item] += 1
        arr = set(arr)
        count = 0
        for item in arr:
            if (item-1) in itemArrCount:
                count += itemArrCount[item-1]
        return count

solution = Solution()
print(solution.countElements([1,2,3]))
print(solution.countElements([1,1,3,3,5,5,7,7]))
print(solution.countElements([1,3,2,3,5,0]))
print(solution.countElements([1,1,2,2]))