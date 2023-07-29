class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sumation=0
        for num in str(n):
            product*=int(num)
            sumation+=int(num)
        return product-sumation
        
        