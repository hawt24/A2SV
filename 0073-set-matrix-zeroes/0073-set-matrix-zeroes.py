class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        roww,coll=[],[]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    roww.append(row)
                    coll.append(col)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in roww or j in coll:
                    matrix[i][j]=0
                    
                        
                        
                        