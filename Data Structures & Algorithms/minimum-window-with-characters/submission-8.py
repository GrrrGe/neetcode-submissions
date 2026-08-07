class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count1 = Counter(t)
        count2 = count1.copy()
        l=0
        need = len(count1)
        resLen = float('inf')
        res = [-1,0]
        for r in range(len(s)):
            if s[r] in count1:
                count2[s[r]]-=1
                if count2[s[r]]==0:
                    need-=1
            while l<=r and need ==0:
                # print(str(l)+" "+str(r))
                # if res[0]!=-1:
                #     print(s[res[0]:res[1]+1])
                if r-l+1<resLen:
                    resLen = r-l+1
                    res = (l,r)
                    
                if s[l] in count1:
                    count2[s[l]]+=1
                    if count2[s[l]]==1:
                        need+=1
                        l+=1
                        break
                l+=1
        if res[0]==-1:
            return ""
        return s[res[0]:res[1]+1]

