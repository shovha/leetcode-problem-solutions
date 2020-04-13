from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remaining = 0
        for i in range(len(nums) - 1):
            remaining = max(remaining-1, nums[i])
            if remaining == 0:
                return False                 
        return remaining >= 1 if len(nums) > 1 else True
        
solution = Solution()
print(solution.canJump([0]))  # True
print(solution.canJump([4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]))  # True
print(solution.canJump([5,9,3,2,1,0,2,3,3,1,0,0])) #True
print(solution.canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5])) #true
print(solution.canJump([4,0,4,2,2,0,1,3,3,0,3])) #true
print(solution.canJump([1,1,2,2,0,1,1])) #true
print(solution.canJump([3,0,8,2,0,0,1])) #true
print(solution.canJump([2,0,0])) #true
print(solution.canJump([2,3,1,1,4])) #true
print(solution.canJump([3,2,1,0,4])) #false
