class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if len(mat)==1:
            if mat==target:
                return True
            return False
        

        for i in range(4):
            mat.reverse()
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                    if mat==target:
                        return True
                    
        return False
                    