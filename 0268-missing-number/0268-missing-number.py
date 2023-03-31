class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #     n=len(nums)
        #     missed=0
        #     summ=int((n*(n+1))/2) #arthematic progression
        #     for i in nums:
        #         missed+=i
        #     return summ-missed
        
        # i=0
        # n=len(list)
        # while(i<n):
        #     if(i==list[i]):
        #         i+=1
        #     elif(list[i]>=n):
        #         flag=i
        #         i+=1
        #     else:
        #         correct= list[i]
        #         list[i],list[correct] =list[correct],list[i]
        # return flag
        
        # counter = [iterator for iterator in range(len(nums)+1)]
        # print(counter)
        
        total=0
        actual_num=0
        for i in range(len(nums)):
            total^=i
            actual_num^=nums[i]
        total^=len(nums)
        return total^actual_num
            

   
        
        
        