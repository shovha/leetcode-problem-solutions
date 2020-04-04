from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        localMax = 0
        for num in nums:
            if num > localMax+num:
                localMax = num
            else:    
                localMax += num
            if localMax > max:
                max=localMax    
        return max

solution = Solution()
print(solution.maxSubArray([2]))