class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans=[]
    
        arr=[(nums[i],i) for i in range(len(nums))]
        arr.sort(reverse=True)
        arr=arr[:k]
        arr.sort(key=lambda k: k[1])
        for i,j in arr:
            ans.append(i)
        
        return ans