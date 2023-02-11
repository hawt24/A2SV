class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left=0
        right=n
        ans=[]
        while left<n and right<len(nums):
            ans.append(nums[left])
            ans.append(nums[right])
            right+=1
            left+=1
        return ans
            