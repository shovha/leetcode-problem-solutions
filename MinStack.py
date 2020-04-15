from typing import List

class MinStack:
    stack=None
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]    
        

    def push(self, x: int) -> None:
        if(len(self.stack)==0):
            self.stack.append({'val':x, 'min':x})
        else:
            self.stack.append({'val':x, 'min':min(x,self.stack[-1]['min'])})

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]['val']
        return None

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]['min']
        return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())