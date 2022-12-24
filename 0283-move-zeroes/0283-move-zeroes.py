class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[start_index]
                nums[start_index]=nums[i]
                nums[i]=temp
                start_index+=1
      
