class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        x = 0
        i = 0
        while num:
            if num % 2 == 1:
                x = 0;
            else:
                x = 1;
            ans += pow(2, i) * x
            num //= 2
            i += 1
        return ans