class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        if len(s2)<len(s1):
            return False
        for c in s1:
            count[c]+=1
        need = len(s1)
        countTemp = count.copy()
        for r in range(len(s2)):
            while r<len(s2) and countTemp[s2[r]]:
                countTemp[s2[r]]-=1
                need-=1
                r+=1
            if need>0:
                need = len(s1)
                countTemp = count.copy()
            elif need==0:
                return True
        return False
