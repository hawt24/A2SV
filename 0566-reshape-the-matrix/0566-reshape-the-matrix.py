class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp=[]
        ans=[]
        for row in mat:
            for col in row:
                temp.append(col)
        print(temp)
        if c*r!=len(temp):
            return mat
        else:
            for i in range (r):
                ans.append(temp[i*c:i*c+c])
            return ans
            
     