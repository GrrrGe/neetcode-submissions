# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkValidity(self, root, Min, Max) -> bool:
        if not root:
            return True
        if root.val <= Min or root.val>=Max:
            return False
        return self.checkValidity(root.left,Min,root.val) and self.checkValidity(root.right,root.val,Max)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        Min = float('-inf')
        Max = float('inf')
        return self.checkValidity(root,Min,Max)

        