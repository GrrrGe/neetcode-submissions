class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        res = 0
        keys = self.points.keys()
        for x,y in keys:
            q1,q2 = point
            if abs(q1-x)==abs(q2-y) and q1!=x:
                if (q1,y) in self.points and (x,q2) in self.points:
                    res+=self.points[(q1,y)]*self.points[(x,q2)]*self.points[(x,y)]
        return res

        
