class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        l,r = 1,len(nums)-2
        dp = {}
        def dfs(l,r):
            if (l,r) in dp:
                return dp[(l,r)]
            res = 0
            for i in range(l,r+1):
                total = nums[l-1]*nums[i]*nums[r+1]
                total +=dfs(l,i-1)+dfs(i+1,r)
                res = max(res,total)
            dp[(l,r)]=res
            return res
        return dfs(l,r)