class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x,y = 0,len(matrix)-1
        row = 0
        l,r = 0, len(matrix[0])-1
        while x<=y:
            row = (y-x)//2 + x
            if matrix[row][l]== target:
                return True
            elif matrix[row][l] < target:
                if matrix[row][r]>= target:
                    break
                x = row+1
            else :
                # if matrix[row][r]target:
                #     break
                y = row -1
        
        while l<=r:
            mid = (r-l)//2 +l
            if matrix[row][mid]== target:
                return True
            elif matrix[row][mid]< target:
                l=mid+1
            else:
                r=mid-1
        return False
