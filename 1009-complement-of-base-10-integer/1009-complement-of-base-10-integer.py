class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        ans = 0
        x = 0
        i = 0
        while n:
            if (n % 2 == 1):
                x = 0;
            else:
                x = 1;
            ans += pow(2, i) * x
            n //= 2;
            i += 1;
        return ans