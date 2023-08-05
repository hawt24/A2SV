class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_dist = 0
        for i in range(1, len(points)):
            x_dist = abs(points[i][0] - points[i-1][0])
            y_dist = abs(points[i][1] - points[i-1][1])

            total_dist += min(x_dist, y_dist) + abs(x_dist - y_dist)

        return total_dist
        