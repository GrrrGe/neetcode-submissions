# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {}
        # for i,e in enumerate(inorder):
        #     cache[e]=i
        if len(preorder)==0:
            return None
        l,r = 0,len(inorder)
        p = preorder[0]
        node = TreeNode(p)
        mid = inorder.index(p)
        l_size = mid - l + 1
        r_size = r - mid +1
        node.left = self.buildTree(preorder[1:1+mid],inorder[0:mid])
        node.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return node