class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[-k]
              
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapify(nums)
        print(nums)
        
        ans = 0
        while k>0:
            ans = -heappop(nums)
            k -= 1
        return ans
      