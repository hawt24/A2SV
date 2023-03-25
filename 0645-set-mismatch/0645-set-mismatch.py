class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s,n=set(nums),len(nums)
        summ=sum(nums)
        A_sum=(n*(n+1))//2
        diff=A_sum-summ
        for i in range(1,n+1):
            if i not in s:
                ans=i
                break
        return ans-diff,ans
