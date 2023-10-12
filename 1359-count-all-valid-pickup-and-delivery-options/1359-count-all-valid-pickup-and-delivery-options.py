class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1

        if n >= 3:
            ans *= factorial(n - 1)

        base = 1
        curr = 2 * n - 1
        while curr > 1:
            base *= curr
            curr -= 2
        
        base *= n
        base *= ans

        return base % (10 ** 9 + 7)