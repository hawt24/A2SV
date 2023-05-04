class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones)==1:
        #     return stones[0]
        for i in range(len(stones)):
            stones[i]*=-1
            
        heapify(stones)    
        while stones:
            while len(stones)>1:
                x=heappop(stones)
                y=heappop(stones)
                heappush(stones,x-y)
            else:
                return -stones[0]
        return 0
    
          
    
        
      
        
        
        