class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        
        res = [0]*(len(num1)+len(num2))
        num1,num2 = num1[::-1],num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = (ord(num1[i1])-ord('0'))*(ord(num2[i2])-ord('0'))
                res[i1+i2]+=digit
                res[i1+i2+1]+=res[i1+i2]//10
                res[i1+i2]=res[i1+i2]%10
        
        while res[-1]==0:
            res.pop()
        

        output = ""
        for c in res[::-1]:
            output+=str(c)
            
        # res = map(str,res)
        return output