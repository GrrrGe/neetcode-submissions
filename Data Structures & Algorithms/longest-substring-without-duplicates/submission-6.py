class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        charSet = defaultdict(int)
        res = 0
        l,r = 0,0
        for r in range(len(s)):
            if s[r] in seen:
                while s[l]!=s[r]:
                    charSet[s[l]]-=1
                    if  charSet[s[l]]==0:
                        seen.remove(s[l])
                    l+=1
                l+=1
            else:
                seen.add(s[r])
                charSet[s[r]]+=1
            res = max(res,len(seen))
        return res