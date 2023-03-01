class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            result=power(x,n//2)
            result=result*result
            if n%2:
                return result*x
            else:
                return result
        result=power(x,abs(n))
        if n>=0:
            return result
        else:
            return 1/result
    
    
            
        
        