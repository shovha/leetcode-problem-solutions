from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]):
        """
        Do not return anything, modify arr in-place instead.
        """
        arrLen = len(arr)
        index = 0
        while index < arrLen:
            if(arr[index] == 0):
                for i in range(arrLen-1,index,-1):
                    arr[i] = arr[i-1]
                i=None
                index += 1
            index += 1


solution = Solution()
print(solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(solution.duplicateZeros([1, 2, 3]))