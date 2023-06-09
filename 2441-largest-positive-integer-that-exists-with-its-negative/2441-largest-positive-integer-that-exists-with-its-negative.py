class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        flag=False
        ans=0
        nums=sorted(nums,reverse=True)
        
        for i in nums:
            if -1*i in nums:
                flag=True
                ans=i
                break
        if flag:
            return ans
        else:
            return -1
            
            

