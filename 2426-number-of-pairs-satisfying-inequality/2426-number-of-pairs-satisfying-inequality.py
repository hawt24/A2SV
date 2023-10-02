class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        temp=[a-b for a,b in zip(nums1,nums2)]
        arr=[]
        ans=0
        
        for i in temp:
            cnt=bisect_right(arr,i)
            ans+=cnt
            bisect.insort(arr,i-diff)
        return ans
        
        