class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry =0
        for i in range(len(digits)-1,-1,-1):
            carry=0
            if digits[i]==9:
                digits[i]=0
                carry=1
            else:
                digits[i]+=1
                break
        if carry:
            digits.insert(0,1)
        return digits