class Solution:
    def isHappy(self, n: int) -> bool:
        total=0
        seen = set()
        while total!=1:
            total=0
            while n:
                digit = n%10
                total+=digit*digit
                n = n//10
            n=total
            if total in seen:
                return False
            seen.add(total)
        return True