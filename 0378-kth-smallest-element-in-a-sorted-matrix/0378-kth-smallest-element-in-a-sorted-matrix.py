class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heap.append(matrix[i][j])
                
        heapify(heap)
        ans=0
        while k>0:
            ans=heappop(heap)
            k-=1
        return ans
        
                
        
                
                
            
                
                
                

                