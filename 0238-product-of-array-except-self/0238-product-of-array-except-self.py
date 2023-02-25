class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        ans=[]
        for i in nums:
            ans.append(product)
            product*=i
        product=1
        for i in reversed(range(len(nums))):
            ans[i]*=product
            product*=nums[i]
        return ans
            
            
            
            
        
        
     
        
    