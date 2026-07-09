class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = 0
        right = 0
        res = []
        cur = []
        def dfs(l,r):
            if l==n and r==n:
                
                res.append("".join(cur))
                # cur.pop()
                return
            
            if l<n:
                cur.append("(")
                dfs(l+1,r)
                cur.pop()
            if r<l:
                cur.append(")")
                dfs(l,r+1)
                cur.pop()
        dfs(0,0)
        return res
            