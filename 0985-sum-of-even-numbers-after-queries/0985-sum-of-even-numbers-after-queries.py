class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_=0
        ans=[]
        for i in nums:
            if i%2==0:
                sum_+=i
        for i in range(len(queries)):
            val,indx=queries[i]
            if nums[indx]%2==0:
                sum_-=nums[indx]
            nums[indx]+=val
            if nums[indx]%2==0:
                sum_+=nums[indx]
                print(sum_)
            ans.append(sum_)
        return  ans
      
        
                
                
                
                
        