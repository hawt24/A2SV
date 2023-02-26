class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        cnt1=0
        cnt2=0
        start=0
        end=0
        while end<len(nums):
            if nums[end]%2!=0:
                cnt1+=1
                cnt2=0
            while cnt1==k:
                if nums[start]%2!=0:
                    cnt1-=1
                cnt2+=1
                start+=1
            ans+=cnt2
            end+=1
        return ans
                
                
