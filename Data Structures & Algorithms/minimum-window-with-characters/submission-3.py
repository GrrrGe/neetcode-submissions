class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        l = 0
        res = (-1,-1)
        Len = float("infinity")
        freq,window = defaultdict(int),defaultdict(int)
        for c in t:
            window[c] +=1
        have, need = 0 , len(window)
        for r in range(len(s)):
            freq[s[r]]+=1
            if s[r] in window and freq[s[r]]==window[s[r]]:
                have+=1
            while have == need:
                if r-l+1<Len:
                    Len = r-l+1
                    res = (l,r)
                freq[s[l]]-=1
                if s[l] in window and freq[s[l]]<window[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1]
