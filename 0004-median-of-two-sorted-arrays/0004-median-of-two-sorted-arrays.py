class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=nums1+nums2
        ans.sort()
        if len(ans)%2!=0:
            return ans[len(ans)//2]
        else:
            a=ans[len(ans)//2]
            b=ans[(len(ans)-1)//2]
            return (a+b)/2