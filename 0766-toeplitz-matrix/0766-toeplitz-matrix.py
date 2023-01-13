class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic=defaultdict(set)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dic[col-row].add(matrix[row][col])
    
        for key,val in dic.items():
            if len(val)>1:
                return False
        return True
            
            
    
                
                