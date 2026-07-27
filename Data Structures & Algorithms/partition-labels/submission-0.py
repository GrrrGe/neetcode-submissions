class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # count = Counter(s)
        lastPos = {}
        for i,c in enumerate(s):
            lastPos[c]=i
        res = []
        end = 0
        start = 0
        for i in range(len(s)):
            end = max(end,lastPos[s[i]])
            if i==end:
                res.append(end-start+1)
                start=end+1
        return res

            
