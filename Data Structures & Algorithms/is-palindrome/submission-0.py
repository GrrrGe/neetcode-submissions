class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for c in s:
            if c.isalnum():
                c = c.lower()
                ans.append(c)
        print(ans)
        i ,j = 0 ,len(ans) -1
        while i<=j:
            if ans[i] != ans[j]:
                return False
            i+=1
            j-=1
        return True
        