"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            root = Node(node.val)
            visited[node] = root
            for child in node.neighbors:
                root.neighbors.append(dfs(child))
            return root
        return dfs(node)

        