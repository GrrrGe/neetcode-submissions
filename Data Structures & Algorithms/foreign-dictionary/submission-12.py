class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        if not words:
            return ""

        adj = defaultdict(set)
        # res = ['a','b']
        # print(res)
        # print(adj)
        letters = set()
        for word in words:
            for c in word:
                letters.add(c)
        
        for r in range(1,len(words)):
            if not self.compare(words[r-1],words[r],adj):
                return ""
        visited = set()
        visiting = set()
        res = []
        def dfs(c)->bool:
            if c in visited:
                return True
            if c in visiting:
                return False
            # visited.add(c)
            # res.append(c)
            # print(c)

            # if c not in adj:
                # print("return true c not in adj")
            #     return True
            
            visiting.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        if not dfs(words[0][0]):
            # print("dfs false")
            return ""
        
        # print(letters)
        # print(res)
        for l in letters:
            if l not in visited and not dfs(l):
                return ""
        return "".join(res[::-1])


    def compare(self,s1,s2,adj)->bool:
        n = len(s1) if len(s1)< len(s2) else len(s2)
        for r in range(n):
            if s1[r]!=s2[r]:
                self.addEdge(s1[r],s2[r],adj)
                return True
        if len(s1)> len(s2):
            return False
        else:
            return True
    
    def addEdge(self,c1,c2,adj):
        adj[c1].add(c2)

        

