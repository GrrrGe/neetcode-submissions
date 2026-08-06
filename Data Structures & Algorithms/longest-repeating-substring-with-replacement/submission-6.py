class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxf = 0
        res = 0
        l= 0
        for r in range(len(s)):
            count[s[r]]+=1
            maxf= max(maxf,max(count.values()))
            if (r-l+1)-maxf<=k:
                res = max(res,r-l+1)
            else:
                while l<r and (r-l+1)-max(count.values())>k:
                    count[s[l]]-=1
                    l+=1
        return res