class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        prefix = strs[0]
        if len(prefix)==0:
            return ""
        longest = len(prefix)
        for s in strs:
            longest = min(len(s),longest)
            for i in range(0,longest):
                if s[i]!=prefix[i]:
                    longest = i
                    break
        return prefix[:longest]
        