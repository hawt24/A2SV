from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # arr=[0]*len(nums)
        # # for i in range(len(nums)):
        #     cnt=0
        #     for j in range(i,len(nums)):
        #         if nums[i]>nums[j]:
        #             cnt+=1
        #     arr[i]=cnt
        # return arr
        """when using append list is use time compexity of o(n) but we can use soretdlist from m           sorted continer so the add in this list is the complexity is O(logn)  beacause the index is         found"""
        temp=SortedList([])
        ans=[]
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]
            idx=temp.bisect_left(num)
            ans.append(idx)
            temp.add(num)
        
        return ans[::-1]
            
        
        
    