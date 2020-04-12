class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sList=[]
        for item in S:
            if(item=='#'):
                if(len(sList)>0):
                    sList.pop()
            else:
                sList.append(item)
        S="".join(sList)

        tList=[]
        for item in T:
            if(item=='#'):
                if(len(tList)>0):
                    tList.pop()
            else:
                tList.append(item)
        T="".join(tList)

        return S==T

        #leetcode solution
        # class Solution(object):
        #     def backspaceCompare(self, S, T):
        #         def build(S):
        #             ans = []
        #             for c in S:
        #                 if c != '#':
        #                     ans.append(c)
        #                 elif ans:
        #                     ans.pop()
        #             return "".join(ans)
        #         return build(S) == build(T)

solution=Solution()
print(solution.backspaceCompare("ab#c","ad#c"))
print(solution.backspaceCompare("a#","c####d#"))
print(solution.backspaceCompare("a##c#c#","cccc####"))
print(solution.backspaceCompare("a#c","b"))

