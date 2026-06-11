class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            if c in m:
                if stack:
                    if stack[-1] != m[c]:
                        return False
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not len(stack)