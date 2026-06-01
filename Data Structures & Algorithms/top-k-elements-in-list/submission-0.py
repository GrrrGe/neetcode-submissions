class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        sorted_items = { k:i for k,i in sorted(count.items(), key=lambda item: item[1], reverse = True)}
        ans = []
        for i,ele in enumerate(sorted_items):
            if i == k:
                break
            ans.append(ele)
        return ans