class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if i %2==0:
                ans.insert(0,i)
            else:
                ans.append(i)
        return ans