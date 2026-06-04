class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        for i in range(len(nums)):
            rem = -nums[i]
            # j = i+1
            num_to_ind = {}
            for j in range(i+1,len(nums)):
                target = rem - nums[j]
                if target in num_to_ind:
                    ans.add(tuple(sorted([nums[i],nums[j],target])))
                else:
                    num_to_ind[nums[j]] = j
        return list(ans)


