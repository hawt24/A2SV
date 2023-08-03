class Solution:
    def pivotInteger(self, n: int) -> int:
        ans= sqrt((n ** 2 + n) // 2)
        return int(ans) if ans.is_integer() else -1
        