# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(root) -> int:
            if not root:
                return 0
            nonlocal maxSum
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            maxSum = max(maxSum,left+right+root.val)
            return root.val + max(left,right)

        dfs(root)
        return maxSum