# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            
        heap = []
        q = deque([root])
        while(q):
            for _ in range(len(q)):
                node = q.popleft()
                heapq.heappush(heap,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        n = -1
        while k > 0:
            n = heapq.heappop(heap)
            k -=1
        return n