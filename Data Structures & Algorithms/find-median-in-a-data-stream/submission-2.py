class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr = sorted(self.arr)
        median = 0.0
        size = len(self.arr)
        if size%2==0:
            median = (self.arr[size//2] + self.arr[size//2-1])/2
        else:
            median = self.arr[size//2]
        return median


        
        