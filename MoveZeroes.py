from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #my solution
        #
        # for index in range(len(nums)):
        #     if(nums[index]==0):
        #         nums.remove(0)
        #         nums.append(0)


        #two pointer approach
        lastNonZeroNumber = 0
        for index in range(len(nums)):
            if(nums[index] != 0):
                nums[lastNonZeroNumber],nums[index] = nums[index],nums[lastNonZeroNumber]
                lastNonZeroNumber +=1
        print(nums)    


solution = Solution()
solution.moveZeroes([0,1,0,3,12])