class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        subset = []
        nums.sort()
        def dfs(i,target):
            if i>= len(nums):
                return
            target -= nums[i]
            if target<0:
                return
            subset.append(nums[i])
            if target == 0:
                if tuple(subset) not in res:
                    res.add(tuple(subset.copy()))
            dfs(i,target)
            subset.pop()
            target += nums[i]
            dfs(i+1,target)
        dfs(0,target)
        return list(list(n) for n in res)


                

