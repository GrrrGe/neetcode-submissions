class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        print(ans)
        return ans


    def decode(self, s: str) -> List[str]:
        i = 0
        ans =[]
        while i < len(s):
            j = i+1
            while s[j]!="#":
                j+=1
            n = int(s[i:j])
            i=j+1
            ans.append(s[i:i+n])
            i+=n
        return ans


