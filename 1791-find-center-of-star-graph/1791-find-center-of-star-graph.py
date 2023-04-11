class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp1=set()
        temp2=set()
        for i,j in edges:
            temp1.add(i)
            temp2.add(j)
        temp=temp1.intersection(temp2)
        if temp:
            return list(temp)[0]
        else:
            if len(temp1)>len(temp2):
                return list(temp2)[0]
            else:
                return list(temp1)[0]
                
                
            
    
        
            