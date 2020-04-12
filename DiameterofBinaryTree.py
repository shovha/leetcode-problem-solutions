# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    maxDepth=0
    def diameterOfBinaryTree(self, root: TreeNode,isfirstIter=True) -> int:
        #leetcode solution
        # self.ans = 1
        # def depth(node):
        #     if not node: return 0
        #     L = depth(node.left)
        #     R = depth(node.right)
        #     self.ans = max(self.ans, L+R+1)
        #     return max(L, R) + 1

        # depth(root)
        # return self.ans - 1
        
        if(root is None):
            return 0
        
        if(root.left is None):
            lDepth=0
        else:    
            lDepth=self.diameterOfBinaryTree(root.left,False)+1

        if(root.right is None):
            rDepth=0
        else:    
            rDepth=self.diameterOfBinaryTree(root.right,False)+1

        if(self.maxDepth<lDepth+rDepth):
            self.maxDepth=lDepth+rDepth
            
        if(isfirstIter):
            return self.maxDepth
        elif(lDepth>rDepth):
            return lDepth
        else:
            return rDepth
        
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
# root.right.left=TreeNode(6)

solution=Solution()
print(solution.diameterOfBinaryTree(root))