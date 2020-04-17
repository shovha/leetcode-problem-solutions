class Solution:
    def checkValidString(self, s: str) -> bool:
        if s == '':
            return True
        s = list(s)
        leftParenthesisIndexList = []
        starIndexList = []
        noOfRightParenthesis = 0
        for index in range(len(s)):
            if(s[index] == '('):
                leftParenthesisIndexList.append(index)
            elif(s[index] == '*'):
                starIndexList.append(index)
            else:
                if(len(leftParenthesisIndexList) > 0):
                    s[leftParenthesisIndexList.pop()] = ''
                    s[index] = ''
                elif(len(starIndexList) > 0):
                    s[starIndexList.pop()] = ''
                    s[index] = ''
                else:
                    noOfRightParenthesis += 1
        if(noOfRightParenthesis > 0):
            return False
        
        startLen=len(starIndexList)
        leftLen=len(leftParenthesisIndexList)
        if(leftLen == 0):
            return True
        if(leftLen>startLen):
            return False    
        
        leftParenthesisIndexList.reverse()
        for index in leftParenthesisIndexList:
            lastStar=starIndexList.pop()
            if(index>lastStar):
                return False
        return True
        # while length:
        #     print(starIndexList)
        #     length -= 1
        # return True
        # return False if '(' in s else True


solution = Solution()
print(solution.checkValidString(
    "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))
# print(solution.checkValidString('(*)'))
# print(solution.checkValidString('(*))'))
# print(solution.checkValidString('(()))*)'))
# print(solution.checkValidString('(((((())))*'))
