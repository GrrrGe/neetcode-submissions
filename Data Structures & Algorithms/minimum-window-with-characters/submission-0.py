class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        l=0
        count = defaultdict(int)
        for c in t:
            count[c]+=1
        
        res = [-1,-1]
        resLen = float("infinity")
        for i in range(len(s)):
            s_count = defaultdict(int)
            for j in range(i,len(s)):
                s_count[s[j]]+=1
                
                flag = True
                for c in count:
                    if count[c] > s_count[c]:
                        flag = False
                        break
                
                if flag:
                    if(j-i+1 < resLen):
                        resLen = j-i+1
                        res = [i,j]
        
            
        i,j = res
        return s[i:j+1] if resLen != float("infinity") else ""




            
        