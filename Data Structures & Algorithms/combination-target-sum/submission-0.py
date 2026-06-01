class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =[]
        def dfs(nums: List[int],cand: List[int], curr:int,start:int):
            for j in range(start,len(nums)):
                i=nums[j]
                temp = cand[:]
                if curr - i == 0:
                    temp.append(i)
                    result.append(temp)
                elif curr - i > 0:
                    temp.append(i)
                    dfs(nums,temp,curr -i,j)
        
        dfs(nums,[],target,0)
        return result

