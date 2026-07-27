class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars= []
        for i,c in enumerate(s):
            if c =='(':
                stack.append(i)
            elif c==')':
                if stack:
                    stack.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
            else:
                stars.append(i)
        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
            stars.pop()
        return len(stack)==0

        