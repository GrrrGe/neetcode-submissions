class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i+1
            while s[j]!="#":
                j+=1
            n = int(s[i:j])
            i = j + 1
            res.append(s[i:i+n])
            i+=n
        return res