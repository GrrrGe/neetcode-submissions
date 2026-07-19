class Solution:
    def countSubstrings(self, s: str) -> int:
        # l,r = 0,0
        # ans = [l,r]
        # for r in range(len(s)):
        #     if self.isPali(s,l,r):
        #         if ans[1]-ans[0]+1 <r-l+1:
        #             ans = [l,r]
        if not s:
            return ""
        n = len(s)
        count = 0
        for i in range(0,n):
            l,r = i,i
            while l>=0 and r<n:
                if s[l]!=s[r]:
                    break
                count+=1
                l-=1
                r+=1
            l,r = i-1,i
            while l>=0 and r<n:
                if s[l]!=s[r]:
                    break
                count+=1
                l-=1
                r+=1
        return count
        
                