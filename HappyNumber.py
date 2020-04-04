class Solution:
    def isHappy(self, n: int) -> bool:
        #
        # my solution
        #
        trackLoop={}
        while True:    
            numList = [int(x)**2 for x in str(n)]
            n = sum(numList)
            if(n==1):
                return True
            elif(n in trackLoop):
                return False    
            else:
                trackLoop[n]=n        



        # two pointer solution
        
        # walker = n
        # runner = sum([int(x)**2 for x in str(n)])
        # while runner != walker:
        #     runner = sum([int(x)**2 for x in str(runner)])
        #     runner = sum([int(x)**2 for x in str(runner)])
        #     walker = sum([int(x)**2 for x in str(walker)])

        # return walker == 1

solution = Solution()
print(solution.isHappy(19))