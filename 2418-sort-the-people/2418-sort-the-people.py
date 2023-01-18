class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            minm=i
            for j in range(i+1,len(heights)):
                if heights[minm]<heights[j]:
                    minm=j
            heights[i],heights[minm]=heights[minm],heights[i]
            names[i],names[minm]=names[minm],names[i]
        return names

            
           
        

                        
        
        
            
        
        
       
    