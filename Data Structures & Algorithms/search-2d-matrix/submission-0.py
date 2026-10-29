class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        top=0
        bottom=row-1
        left=0
        right=col-1
        while top<=bottom:
            m1=(top+bottom)//2
            if target<matrix[m1][0]:
                bottom=m1-1
            elif target>matrix[m1][col-1]:
                top=m1+1
            else:
                while left<=right:
                    m2=(left+right)//2
                    if matrix[m1][m2]>target:
                        right=m2-1 
                    elif matrix[m1][m2]<target:
                        left=m2+1
                    else:
                        return True
                return False
        return False

        
        