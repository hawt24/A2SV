class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        currsum=0
        curr={0:1}
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum-k in curr:
                count+=curr[currsum-k]
            if currsum in curr:
                curr[currsum]+=1
            else:
                curr[currsum]=1
        return count
            
                          
                          
                          
                          
                          

        