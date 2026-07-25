class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            res = False
            if i>=len(s) and j >= len(p):
                return True
            elif i>=len(s) or j>=len(p):
                if j+1<len(p) and p[j+1]=='*':
                    res = res or dfs(i,j+2)
                    dp[(i,j)] = res
                    return res
                else:
                    return False
            if j+1<len(p) and p[j+1]=='*':
                res  = res or dfs(i,j+2)
                if s[i]==p[j] or p[j]=='.':
                    res = res or dfs(i+1,j)
                    res = res or dfs(i+1,j+2)
            elif s[i]==p[j] or p[j]=='.':
                res = res or dfs(i+1,j+1)
            dp[(i,j)] = res
            return res


        return dfs(0,0)
            
