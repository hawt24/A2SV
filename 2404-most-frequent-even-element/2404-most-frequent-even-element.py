class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        c = Counter(filter(lambda n: n % 2 == 0, nums))
        if c:
            return c.most_common()[0][0]
        else:
            return -1