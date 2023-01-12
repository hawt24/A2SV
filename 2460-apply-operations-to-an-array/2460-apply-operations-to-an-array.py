class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            ans.append(nums[i])
        ans.append(nums[-1])
                
        start_index=0
        for i in range(len(ans)):
            if ans[i]!=0:
                temp=ans[start_index]
                ans[start_index]=ans[i]
                ans[i]=temp
                start_index+=1
        return ans