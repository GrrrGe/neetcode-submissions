# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0
        def dfs(highest, root):
            if not root:
                return
            if root.val >= highest:
                nonlocal res
                res+=1
                highest = root.val
            
            dfs(highest,root.left)
            dfs(highest,root.right)
        
        dfs(-101,root)
        return res
            


        

        