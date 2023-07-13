class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num = Counter(nums)
        ans=sorted(nums, key=lambda x: (num[x], -x))
        return ans