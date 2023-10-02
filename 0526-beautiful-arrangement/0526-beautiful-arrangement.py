class Solution:
    def countArrangement(self, n: int) -> int:
        arr = [False] * (n + 1)
        cnt = 0

        def backtrack(x):
            nonlocal cnt

            if x == 0:
                cnt += 1

            for i in range(1, n + 1):
                if not arr[i] and (x % i == 0 or i % x == 0):
                    arr[i] = True
                    backtrack(x - 1)
                    arr[i] = False

        backtrack(n)
        return cnt