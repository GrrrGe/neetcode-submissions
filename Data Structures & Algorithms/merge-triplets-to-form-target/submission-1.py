class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.insert(0,[0,0,0])
        for i in range(1,len(triplets)):
            x1,y1,z1 = triplets[i-1]
            x2,y2,z2 = triplets[i]
            nx,ny,nz= max(x1,x2),max(y1,y2),max(z1,z2)
            if nx<=target[0] and ny<=target[1] and nz<=target[2]:
                triplets[i]=[nx,ny,nz]
            else:
                triplets[i]=triplets[i-1]
        if triplets[-1]==target:
            return True
        else:
            return False