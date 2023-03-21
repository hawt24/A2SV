class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            x=list(str(x))
            prev_index=0
            i=len(x)-1
            while prev_index<i:
                temp=x[prev_index]
                x[prev_index]=x[i]
                x[i]=temp
                prev_index+=1
                i-=1
            x=int("".join(map(str, x)))
            return x if x<=2**31 - 1 else 0
        else:
            x=abs(x)
            x=list(str(x))
            prev_index=0
            i=len(x)-1
            while prev_index<i:
                temp=x[prev_index]
                x[prev_index]=x[i]
                x[i]=temp
                prev_index+=1
                i-=1
            x=-1*int("".join(map(str, x))) 
            return x if  x>=-2**31 - 1 else 0
    
            """ans <- 2**31 or ans > 2**31-1:"""
  
   
        


            
        