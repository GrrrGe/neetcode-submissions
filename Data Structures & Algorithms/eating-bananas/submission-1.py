class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        time = 0
        l,max_k = 1,max(piles)
        mid = 0 
        while l<=max_k:
            mid = (max_k-l)//2 + l
            # print("mid:"+str(mid))
            for p in piles:
                # print("p:"+str(p))
                # print("p/k = "+str(math.ceil( p/mid)))
                time+= math.ceil( p/mid)
            if time>h:
                l=mid+1
            else:
                max_k = mid-1
            time=0
                
        return l