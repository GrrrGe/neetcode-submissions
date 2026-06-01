class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref , suff = [0]*n, [0]*n
        pref[0] = nums[0]
        suff[-1] = nums[-1]
        for i in range(1,len(nums)):
            pref[i] = pref[i-1]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            suff[i] = suff[i+1]*nums[i]
        ans = []
        for i in range(len(nums)):
            if i > 0 and i< len(nums) -1:
                ans.append(pref[i-1]*suff[i+1])
            if i == 0:
                ans.append(suff[i+1])
            if i == len(nums)-1:
                ans.append(pref[i-1])
        return ans

        # 1, 2, 4 ,6
        # pref : 1 , 2 , 8, 48
        # suff: 48, 48, 24, 6
        # ans: 