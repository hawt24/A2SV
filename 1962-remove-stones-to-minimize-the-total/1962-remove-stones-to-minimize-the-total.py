class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        Heap = []
        
        for i in range(len(piles)):
            heappush(Heap, -piles[i])

        while k> 0:
            temp =heappop(Heap)
            j = temp//2
            heappush(Heap,j)
            k -= 1
            
        return -sum(Heap)
        
        
                
     

        
    
        
        