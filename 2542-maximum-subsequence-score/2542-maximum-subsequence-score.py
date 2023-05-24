class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap=[]
        curr=0
        ans=0
        num=zip(nums1,nums2)

        sorted_arr=sorted(num,key=lambda x:-x[1])

        
        for num in sorted_arr:
            num1,num2=num
            heappush(heap,num1)
            curr+=num1
            if len(heap)>k:
                curr-= heappop(heap)
            if len(heap)==k:
                ans=max(ans,curr*num2)
                
        return ans
                
            
            