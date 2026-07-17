class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # adj = defaultdict(list)

        visited = set()
        path = []
        q = deque()
        q.append(beginWord)
        count = 0
        while q:
            count+=1
            for r in range(len(q)):
                w = q.popleft()
                if w in visited:
                    continue
                visited.add(w)
                for s in wordList:
                    if self.isConnected(w,s):
                        if s ==endWord:
                            return count+1
                        q.append(s)
        return 0
        # def dfs(s):
        #     if s in visited:
        #         return 0
            
        #     visited.add(s)
        #     for word in wordList:
        #         if self.isConnected(s,word):
        #             path.append(word)
        #             # adj[s].append(word)
        #             if word == endWord:
        #                 return len(path)
        #             dfs(word)
        #             path.pop()
        #     return 0

        # return dfs(beginWord)


    def isConnected(self,s1,s2):
        diff = 0
        for r in range(len(s1)):
            if s1[r]!=s2[r]:
                diff+=1
            if diff>1:
                return False
        return diff==1