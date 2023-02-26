class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        we can solve first in burte force
        ans=0
        for start in len(nums):
             summm=0
             for end in len(sart,len(nums)):
                  summ+=nums[end]
                  if summ%2==0:
                     ans+=1
        return ans
        time complextiy o(n^2)
        space complexity (1)  
        
        but try to find optimal solution
         A------------B
         C--------------------D
         sum(A up to B)%k=x
         sum(C up to D)%k=x
    
         from this between B and D is divisible by K
         
        """
        dic={0:1}
        prefix_sum=0
        ans=0
        for i in range((len(nums))):
            prefix_sum+=nums[i]
            key=prefix_sum%k
            if key in dic:
                ans+=dic[key]
                dic[key]+=1
            else:
                dic[key]=1
        return ans
        
            
        
        

            
       