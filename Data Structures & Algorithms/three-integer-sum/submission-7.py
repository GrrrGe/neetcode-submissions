class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            target = - nums[i]
            l,r = i+1,len(nums)-1
            while l<r:
                total = nums[l]+nums[r]
                if total>target:
                    r-=1
                    continue
                    
                elif total==target:
                    res.append(tuple([nums[i],nums[l],nums[r]]))
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                    
            
        return list(set(tuple(res)))
