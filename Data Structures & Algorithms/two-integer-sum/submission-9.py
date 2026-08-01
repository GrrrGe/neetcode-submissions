class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,n in enumerate(nums):
            if target - n in res and res[target-n]!=i:
                return [res[target-n],i]
            res[n]=i
        return []