class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(n)}

        for node,e in edges:
            preMap[node].append(e)
            preMap[e].append(node)

        # cycle = set()
        visited = set()
        def dfs(prev,node):
            # if node in cycle:
            #     return False
            if node in visited:
                return False
            # cycle.add(node)
            visited.add(node)
            for e in preMap[node]:
                if e==prev:
                    continue
                if not dfs(node,e):
                    return False
            
            # cycle.remove(node)
            # visited.remove(node)
            # cycle.add(node)

            
            return True
        
        if not dfs(-1,0):
            return False
        return len(visited)==n