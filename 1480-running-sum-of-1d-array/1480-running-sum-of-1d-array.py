class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ=0
        ans=[]
        for i in  nums:
            summ+=i
            ans.append(summ)
        return ans