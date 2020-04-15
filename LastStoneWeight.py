from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        length=len(stones)
        while length>1:
            stones=sorted(stones)
            diff=stones.pop()-stones.pop()
            if(diff>0): 
                stones.append(diff)
            length=len(stones)
        return stones[0] if length else 0    

solution=Solution()
print(solution.lastStoneWeight([2,7,4,1,8,10,1]))