import math
import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #my solution
        #
        # nodeArr = []
        # nodeArr.append(head)
        # nextNode=head.next
        # while nextNode!=None:
        #     nodeArr.append(nextNode)
        #     nextNode=nextNode.next
        # nodeLen = len(nodeArr)
        # if(nodeLen%2==0):
        #     return nodeArr[int(nodeLen/2)]
        # return nodeArr[math.floor(nodeLen/2)]
        
        # same solution with less code
        # A = [head]
        # while A[-1].next:
        #     A.append(A[-1].next)
        # return A[len(A) // 2]

        # Fast and Slow Pointer
        slow = fast = head
        print(head.val)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

solution = Solution()
l6 = ListNode(6)
l5 = ListNode(5,l6)
l4 = ListNode(4,l5)
l3 = ListNode(3,l4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)
print(solution.middleNode(l1))