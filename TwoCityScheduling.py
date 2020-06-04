from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        aCityCostSum = 0
        bCityCostRefund = []
        noOfInterviewer = len(costs)

        for i in range(noOfInterviewer):
            aCityCostSum += costs[i][0]
            bCityCostRefund.append(costs[i][1] - costs[i][0]) 

        bCityCostRefund = sorted(bCityCostRefund)[0:noOfInterviewer//2]
        
        return aCityCostSum + sum(bCityCostRefund)

solution = Solution()
print(solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))