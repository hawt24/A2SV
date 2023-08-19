class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(n):
            sum_ = 0
            while n > 0:
                sum_ += n % 10
                n //= 10
            return sum_
        hashMap = {}
        for x in range(1, n+1):
            dsum = digit_sum(x)
            if dsum in hashMap:
                hashMap[dsum] += 1
            else:
                hashMap[dsum] = 1
        max_ = max(hashMap.values())
        cnt = 0
        for _, v in hashMap.items():
            if max_ == v:
                cnt += 1
        return cnt