class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<len(nums2):
            A,B = nums1,nums2
        else:
            B,A = nums1,nums2
        
        total = len(A)+ len(B)
        half = total//2
        l,r = 0, len(A)-1

        while True:
            midA = (l+r)//2
            midB = half - (midA+1) - 1
            # midB = 
            Aleft = A[midA] if midA>=0 else float('-inf')
            Aright = A[midA+1] if midA+1< len(A) else float('inf')
            Bleft = B[midB] if midB>=0 else float('-inf')
            Bright = B[midB+1] if midB+1 < len(B) else float('inf')

            if Aleft<= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            
            if Aleft>= Bright:
                r=midA-1
            if Bleft>= Aright:
                l = midA+1
        # return 0
            
