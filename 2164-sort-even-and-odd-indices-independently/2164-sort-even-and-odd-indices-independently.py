class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)
                
        even_nums.sort()
        odd_nums.sort(reverse=True)
        
        sorted_nums = []
        if len(even_nums) >= len(odd_nums):
            for i in range(len(odd_nums)):
                sorted_nums.append(even_nums[i])
                sorted_nums.append(odd_nums[i])
            sorted_nums = sorted_nums + even_nums[len(odd_nums):]
        else:
            for i in range(len(even_nums)):
                sorted_nums.append(even_nums[i])
                sorted_nums.append(odd_nums[i])
            sorted_nums = sorted_nums + odd_nums[len(even_nums):]
            
        return sorted_nums

            
        
            
    
        
        