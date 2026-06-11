class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+','-','*','/'])
        for t in tokens:
            if t in ops:

                e2 = int(stack.pop())
                e1 = int(stack.pop())
                if t == '+':
                    e1 = e1+ e2
                elif t == '-':
                    e1 = e1 - e2
                elif t == '*':
                    e1 = e1*e2
                else:
                    if e2 != 0:
                        e1 = int(e1/e2)
                print("e1: "+str(e1))
                stack.append(str(e1))
            else:
                stack.append(t)
        return int(stack[0])