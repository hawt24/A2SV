class Solution:
    def climbStairs(self, n: int) -> int:
        m, r = n//2, n%2
        res = 1
        for i in range(1, m+1):
            res += comb(n-i, i)
        return res