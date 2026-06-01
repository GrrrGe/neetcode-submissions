class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[1] = 1
        cache[2] = 2
        def dfs(n):
            if n in cache:
                return cache[n]
            cache[n] = dfs(n-1)+ dfs(n-2)
            return cache[n]
        return dfs(n)
