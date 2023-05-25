class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k>=numOnes+numZeros:
            curr=numOnes+(numZeros)
            need_neg=k-curr
            curr-=numZeros
            return curr+(-need_neg)
            
        elif numOnes>k:
            return k
        elif  numOnes+numZeros>k:
            curr=numOnes
            need_zero=k-curr
            return curr+(0*need_zero)
        
            
            
    
            
    