class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1=set(nums1)
        set2=set(nums2)
        ans=set1.intersection(set2)
        if ans:
            return min(ans)
        return -1
        
     
        
        
           