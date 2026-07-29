class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = x
        while n>1:
            x*=num
            n-=1
        while n<=0:
            x/=num
            n+=1
        return x