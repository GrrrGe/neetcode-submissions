class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i==len(s):
                dp[i]=True
                return dp[i]
            for w in wordDict:
                n = len(w)
                if n>len(s):
                    continue
                if s[i:i+n]==w:
                    if dfs(i+n):
                        return True
            dp[i]= False
            return dp[i]
        return dfs(0)
        
