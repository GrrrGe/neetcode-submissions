class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i,j = 0, len(s)-1
        if len(s)==0:
            return True
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
        