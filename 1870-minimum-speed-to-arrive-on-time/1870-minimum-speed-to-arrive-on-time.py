class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        def helper(n):
            time = 0
            for i in dist[:-1]:
                time += math.ceil(i/n)
            time += float(dist[-1]/n)
            if time <= hour:
                return True
            return False

        ans =  float("inf")
        lo, hi = 1, 10**7
        while lo<=hi:
            mid = (lo+hi)//2
            if helper(mid):
                ans = min(ans,mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return ans if ans!=float('inf') else -1
        