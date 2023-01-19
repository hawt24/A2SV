class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic={}
        for idx,val in enumerate(sorted(nums)):
            if val not in dic:
                dic[val]=idx
        
        
        ans=[]
        for idx,val in enumerate(nums):
            ans.append(dic[val])
        return ans
            
        
        