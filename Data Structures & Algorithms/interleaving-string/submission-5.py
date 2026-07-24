class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i,j,k = 0,0,0
        m,n,o = len(s1),len(s2),len(s3)
        if m+n!=o:
            return False
        # for k in range(len(s3)):

        #     if i < len(s1) and s3[k]==s1[i]:
        #         i+=1
        #     elif j < len(s2) and s3[k]==s2[j]:
        #         j+=1
        #     else:
        #         return False
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            k=i+j
            res1, res2 = False,False
            if k>o:
                return False
            if k==o:
                return True
            if i < m and s3[k]==s1[i]:
                res1 = dfs(i+1,j)
            if j < n and s3[k]==s2[j]:
                res2 = dfs(i,j+1)
            dp[(i,j)] = res1 or res2
            return dp[(i,j)]


        return dfs(0,0)