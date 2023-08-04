class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total={}
        for i,num in enumerate(nums):
            sumation=target-num
            if sumation in total:
                return [total[sumation],i]
            else:
                total[num]=i  
        return 
        
          