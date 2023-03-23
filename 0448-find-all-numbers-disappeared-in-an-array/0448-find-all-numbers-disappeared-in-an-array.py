class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=set()
        cheak=set(nums)
        for i in range(1,len(nums)+1):
            if i not in cheak:
                ans.add(i)
        return ans
            


               