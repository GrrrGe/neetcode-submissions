from collections import defaultdict
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

        adj = defaultdict(set)
        letters = set()
        
        for word in words:
            for c in word:
                letters.add(c)

        for r in range(1, len(words)):
            if not self.compare(words[r-1], words[r], adj):
                return ""

        visited = {}  # False = visited, True = current path
        res = []

        def dfs(c) -> bool:
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
            
            visited[c] = False
            res.append(c)
            return False

        for l in letters:
            if l not in visited:
                if dfs(l):
                    return ""

        return "".join(res[::-1])

    def compare(self, s1, s2, adj) -> bool:
        n = min(len(s1), len(s2))
        for r in range(n):
            if s1[r] != s2[r]:
                self.addEdge(s1[r], s2[r], adj)
                return True
        if len(s1) > len(s2):
            return False
        return True

    def addEdge(self, c1, c2, adj):
        adj[c1].add(c2)