class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((queries[i],i) for i in range(len(queries)))
        output = [float('inf')]*len(queries)
        for q in queries:
            for start,end in intervals:
                if start<=q[0]<=end:
                    output[q[1]]=min(output[q[1]],end-start+1)
                    # break
                if start>q[0]:
                    break
            if output[q[1]]==float('inf'):
                output[q[1]]=-1
        return output