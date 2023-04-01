class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # def gcd(x, y):
        #     if y == 0:
        #         return x
        #     else:
        #         return gcd(y, x % y)
        # return gcd(max(nums),min(nums))
        
        for i in range(1,min(nums)+1):
            if max(nums) % i == 0 and min(nums) % i == 0:
                gcd = i
        return gcd
