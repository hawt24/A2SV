class DetectSquares:

    def __init__(self):
        self.point_frequency = defaultdict(int)
        self.points = []
        
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.point_frequency[(*point,)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        count = 0
        
        for x, y in self.points:
            if abs(px - x) == abs(py - y):
                if px != x:
                    count += self.point_frequency[(x, py)] * self.point_frequency[(px, y)]
        
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)