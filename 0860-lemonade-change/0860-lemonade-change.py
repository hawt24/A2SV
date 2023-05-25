class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives,tens,tewens=0,0,0
        
        for i in bills:
            if i==5:
                fives+=1
            elif i==10:
                if fives==0:
                    return False
                tens+=1
                fives-=1
            else:
                if fives>0 and tens>0:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
                tewens+=1
        return True
                    
                
                    
                    
                    
                    

                        
                    
      
                
           
        