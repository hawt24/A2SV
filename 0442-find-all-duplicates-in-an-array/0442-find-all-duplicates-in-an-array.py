class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        ans=[]
        for i in range(len(nums)):
            if cnt[nums[i]]>1:
                ans.append(nums[i])
        return set(ans)
        
        