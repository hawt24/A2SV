class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=[]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans.append(matrix[row][col])
                if target in ans:
                    return True
        return False
                    