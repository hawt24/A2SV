class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_integer = int(''.join(map(str,digits)))
        digits_integer+=1
        return list(map(int,str(digits_integer)))
    
            
    
                    
            
       
            
     