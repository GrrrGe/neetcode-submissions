class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for node,e in edges:
            adj[node].append(e)
            adj[e].append(node)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for e in adj[node]:
                dfs(e)
   
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        
        return count
