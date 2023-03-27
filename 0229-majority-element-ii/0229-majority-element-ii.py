class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for key, val in cnt.items():
            if val >len(nums) // 3:
                ans.append(key)
        return ans



        