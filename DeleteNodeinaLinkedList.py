# Definition for a binary tree node.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# head = [4,5,1,9], node = 5
l9 = ListNode(9)
l1 = ListNode(1,l9)
l5 = ListNode(5,l1)
l4 = ListNode(4,l5)

solution = Solution()
print(solution.deleteNode(l5))