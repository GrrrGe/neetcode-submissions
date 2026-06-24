class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(i,target):
            if i>= len(candidates):
                return
            subset.append(candidates[i])
            target -= candidates[i]
            if target <0:
                subset.pop()
                # while i+1<len(candidates) and candidates[]
                return
            if target == 0:
                res.append(subset.copy())
                subset.pop()
                return
            dfs(i+1,target)
            subset.pop()
            target+=candidates[i]
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1,target)
        dfs(0,target)
        return res
