from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # my solution        
        nums.sort()
        if(len(nums)==1):
            return nums[0]
        for i in range(len(nums)):
            if((i==len(nums)-1)):
                if(nums[i]!=nums[i-1]):   
                    return nums[i]
            elif(nums[i]!=nums[i+1] and nums[i]!=nums[i-1]):
                return nums[i]
        return None    

        # solution 3: Math
        # return 2 * sum(set(nums)) - sum(nums)

        # solution 4: bit manupulation
        # If we take XOR of zero and some bit, it will return that bit
        # a = 0
        # for i in nums:
        #     a ^= i
        # return a


solution = Solution()
print(solution.singleNumber([4,2,2,3,3,3]))
