class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr=[]
        ans=0
        
        for i in nums:
            
            cnt=bisect_right(arr,i*2)
            
            ans+=len(arr)-cnt
            bisect.insort(arr,i)
            
        return ans
        