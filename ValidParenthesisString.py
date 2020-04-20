class Solution:
    def checkValidString(self, s: str) -> bool:
        #Greedy solution
        lo = hi = 0
        print(s)
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            print(lo,hi)
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
        
        # My solution
        #
        # if s == '':
        #     return True
        # s = list(s)
        # leftParenthesisIndexList = []
        # starIndexList = []
        # noOfRightParenthesis = 0
        # for index in range(len(s)):
        #     if(s[index] == '('):
        #         leftParenthesisIndexList.append(index)
        #     elif(s[index] == '*'):
        #         starIndexList.append(index)
        #     else:
        #         if(len(leftParenthesisIndexList) > 0):
        #             s[leftParenthesisIndexList.pop()] = ''
        #             s[index] = ''
        #         elif(len(starIndexList) > 0):
        #             s[starIndexList.pop()] = ''
        #             s[index] = ''
        #         else:
        #             noOfRightParenthesis += 1
        # if(noOfRightParenthesis > 0):
        #     return False
        
        # startLen=len(starIndexList)
        # leftLen=len(leftParenthesisIndexList)
        # if(leftLen == 0):
        #     return True
        # if(leftLen>startLen):
        #     return False    
        
        # leftParenthesisIndexList.reverse()
        # for index in leftParenthesisIndexList:
        #     lastStar=starIndexList.pop()
        #     if(index>lastStar):
        #         return False
        # return True




solution = Solution()
# print(solution.checkValidString(
#     "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))
print(solution.checkValidString('(*)'))
print(solution.checkValidString('((*)'))
# print(solution.checkValidString('(()))*)'))
# print(solution.checkValidString('(((((())))*'))
