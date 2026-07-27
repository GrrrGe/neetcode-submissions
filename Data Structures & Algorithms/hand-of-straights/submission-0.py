class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize:
            return False

        count = Counter(hand)

        for n in sorted(count.keys()):
            curr_count = count[n]
            if curr_count==0:
                continue
            for i in range(n,n+groupSize):
                if count[i]<curr_count:
                    return False
                else:
                    count[i]-=curr_count
        return True