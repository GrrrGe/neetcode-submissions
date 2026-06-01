class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+= 1

        ans = [[] for i in range(len(nums)+1)]
        for key,val in count.items():
            ans[val].append(key)
        
        res = []
        for i in range(len(ans)-1,0,-1):
            for num in ans[i]:
                res.append(num)
                if len(res) == k:
                    return res
