class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count = defaultdict(int)
        for c in t:
            count[c]+=1
        
        s_count = defaultdict(int)
        have , need = 0, len(count)
        res = [-1,-1]
        resLen = float("infinity")
        l =0
        for r in range(len(s)):
            s_count[s[r]]+=1

            if s[r] in count and s_count[s[r]] == count[s[r]]:
                have +=1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                s_count[s[l]]-=1
                if s[l] in count and s_count[s[l]]< count[s[l]]:
                    have-=1
                l+=1


        i,j = res
        return s[i:j+1] if resLen != float("infinity") else ""