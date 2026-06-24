class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        cur = []
        nums.sort()
        def dfs(i):
            if i >=len(nums):
                if tuple(cur) not in res:
                    res.add(tuple(cur.copy()))
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return list(list(r) for r in res)