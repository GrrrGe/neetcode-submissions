# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_dia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root)-> int:
            if not root:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right) 
            dia = lh +rh
            self.max_dia = max(self.max_dia,dia)
            return 1+max(lh,rh)
        
        dfs(root)
        return self.max_dia

        