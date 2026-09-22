# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        first = [p]
        second = [q]

        while first and second:
            nodeF = first.pop()
            nodeS = second.pop()

            if nodeF is None and nodeS is None:
                continue
            
            if nodeF is None or nodeS is None or nodeF.val != nodeS.val:
                return False
            
            first.append(nodeF.left)
            first.append(nodeF.right)

            second.append(nodeS.left)
            second.append(nodeS.right)
        return True