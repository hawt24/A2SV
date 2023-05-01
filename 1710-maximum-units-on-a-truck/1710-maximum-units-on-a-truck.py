class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr=sorted(boxTypes,key= lambda i:i[1],reverse=True)
        summ=0
        ans=0
        temp=0
        for i,j in arr:
            if summ+i<truckSize:
                ans+=i*j
                summ+=i
            elif summ<truckSize:
                ans+=(truckSize-summ)*j
                summ=truckSize
        return ans

            
    
            

 
     
            
            
            
        
      