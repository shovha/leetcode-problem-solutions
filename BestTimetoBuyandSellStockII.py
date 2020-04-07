from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for index in range(1,len(prices)):
            if(prices[index-1] < prices[index]):
                maxProfit += prices[index] - prices[index-1]
        return maxProfit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5]))
print(solution.maxProfit([7,6,4,3,1]))