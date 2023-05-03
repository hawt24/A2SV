class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
              
        # for i in range(len(nums)):
        #     nums[i] *= -1
        
        heapify(nums)
        print(nums)
        
        ans = 0
        temp = len(nums) - k + 1
        while temp > 0:
            ans = heappop(nums)
            temp -= 1
        return ans
      