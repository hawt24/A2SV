class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums.append(int(str(nums[i])[: :-1])) #revere a given number
        return len(set(nums)) #or remove duplicate number use set
          
        
           