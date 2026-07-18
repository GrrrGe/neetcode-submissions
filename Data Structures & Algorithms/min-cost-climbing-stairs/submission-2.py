class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # if not cost[0]:
        #     return 0
        # if cost[1]:
        #     cost[1]=min(cost[1],cost[0])
        for r in range(2,n):
            cost[r]+=min(cost[r-1],cost[r-2])
        
        return min(cost[n-1],cost[n-2])
        