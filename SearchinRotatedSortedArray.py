from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return target        


solution = Solution()
# print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(solution.search([], 0))
# print(solution.search([1], 1))
# print(solution.search([1,2,3], 3))
# print(solution.search([1,3], 0))
print(solution.search([1,3], 3))
