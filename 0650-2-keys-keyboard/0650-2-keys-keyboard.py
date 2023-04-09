class Solution:
    def minSteps(self, n: int) -> int:
        factorization=[]
        d = 2
        while n>1:
            while n%d==0:
                factorization.append(d)
                n=n//d
            d+=1
        return sum(factorization)