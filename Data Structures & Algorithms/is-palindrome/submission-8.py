class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for c in s:
            if c.isalnum():
                t+=c.lower()
        l,r = 0, len(t)-1
        print(t)
        while l<r:
            if t[l]!=t[r]:
                return False
            l+=1
            r-=1
        return True