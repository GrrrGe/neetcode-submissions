class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0]*26
        for s in s1:
            freq[ord(s)-ord('a')]+=1
        if len(s2)<len(s1):
            return False
        l,r = 0,0
        window = [0]*26
        for r in range(len(s1)):
            window[ord(s2[r])-ord('a')]+=1
        if window == freq:
            return True
        for r in range(r+1,len(s2)):
            window[ord(s2[r])-ord('a')]+=1
            window[ord(s2[l])-ord('a')]-=1
            l+=1
            if window == freq:
                return True
            



        return False
