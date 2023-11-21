class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic={}
        for i in range(len(nums)):
            val=(target-nums[i]) 
            if val not in dic:
                 dic[nums[i]]=i
            else:
                 return [i, dic[val]]
        return []
