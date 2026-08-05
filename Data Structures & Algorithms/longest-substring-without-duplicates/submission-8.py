class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l,r = 0,0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            else:
                seen.add(s[r])
            res = max(res,len(seen))
        return res