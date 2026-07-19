class Solution:
    def longestPalindrome(self, s: str) -> str:
        # l,r = 0,0
        # ans = [l,r]
        # for r in range(len(s)):
        #     if self.isPali(s,l,r):
        #         if ans[1]-ans[0]+1 <r-l+1:
        #             ans = [l,r]
        if not s:
            return ""
        n = len(s)
        resLen = 1
        ans=(0,0)
        for i in range(0,n):
            l,r = i,i
            while l>=0 and r<n:
                if s[l]!=s[r]:
                    break
                if r-l+1 > resLen:
                    resLen = r-l+1
                    ans = (l,r)
                l-=1
                r+=1
            l,r = i-1,i
            while l>=0 and r<n:
                if s[l]!=s[r]:
                    break
                if r-l+1 > resLen:
                    resLen = r-l+1
                    ans = (l,r)
                l-=1
                r+=1
        return s[ans[0]:ans[1]+1]
            



    
    def isPali(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        
                