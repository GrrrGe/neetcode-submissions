class Solution:
    def isValid(self, s: str) -> bool:
        bracs = {')':'(', ']':'[','}':'{'}
        stack = []
        if len(s)%2!=0:
            return False
        for c in s:
            if c not in bracs:
                stack.append(c)
            else:
                if not stack or stack[-1] != bracs[c]:
                    return False
                stack.pop()
        return not stack
