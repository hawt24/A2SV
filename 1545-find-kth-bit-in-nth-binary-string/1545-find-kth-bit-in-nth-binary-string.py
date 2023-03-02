class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(x):
            x=x[::-1]
            return x
        def inv(y):
            st=""
            for i in y:
                if i=="0":
                    st+="1"
                else:
                    st+="0"
            return st
        
        
        
        def fun(n):
            if n==1:
                return "0"
            return fun(n-1)+ "1"+rev(inv(fun(n-1)))
        return fun(n)[k-1]
                    
            
            

            
        