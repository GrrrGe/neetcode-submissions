class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        half = total/2
        curSum = 0
        def dfs(i):
            if i==len(nums):
                return False
            nonlocal curSum
            curSum+=nums[i]
            if curSum == half:
                return True
            if dfs(i+1):
                return True
            curSum-=nums[i]
            return dfs(i+1)
        return dfs(0)
