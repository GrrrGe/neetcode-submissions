class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        output = []
        i=0
        while i < len(s):
            length = ""
            while i<len(s) and s[i]!="#":
                length+=s[i]
                i+=1
            if len(length)==0:
                i+=1
                continue
            start = i+1
            end = start+int(length)
            output.append(s[start:end])
            i=end
        return output
