class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI = 0
        resLen = 0
        for i in range(len(s)):
            l,r = i,i
            while l<=r:
                if l<0 or r>=len(s) or s[l]!=s[r]:
                    break
                if r-l+1> resLen:
                    resLen = r-l+1
                    resI = l
                l-=1
                r+=1
            l,r = i,i+1
            while l<=r:
                if l<0 or r>=len(s) or s[l]!=s[r]:
                    break
                if r-l+1> resLen:
                    resLen = r-l+1
                    resI = l
                l-=1
                r+=1
        return s[resI:resI+resLen]
                


