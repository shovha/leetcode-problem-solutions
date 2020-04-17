from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for index in range(n):
            if(nums[index]==0):
                nums[index]=-1
        prefix={}
        prefix[0]=-1
        sum=0
        maxLength=0
        for index in range(n):
            sum += nums[index]
            if(not sum in prefix):
                prefix[sum]=index
            else:
                maxLength=max(maxLength,index-prefix[sum])
        return maxLength

solution=Solution()
print(solution.findMaxLength([1,0,1,0,1])) #4
print(solution.findMaxLength([0,0,0,1,1,1,0])) #6