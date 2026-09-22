# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        first = [p]
        second = [q]

        while first and second:
            first_node = first.pop()
            second_node = second.pop()

            if first_node is None and second_node is None:
                continue
            
            if first_node is None or second_node is None or first_node.val != second_node.val:
                return False
        
            first.append(first_node.left)
            first.append(first_node.right)
            second.append(second_node.left)
            second.append(second_node.right)

                
        return True