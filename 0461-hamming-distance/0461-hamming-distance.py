class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp=bin(x^y)
        return temp.count("1")