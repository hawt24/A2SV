class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=nums.count(0)
        one=nums.count(1)
        two=nums.count(2)
        for i in range(len(nums)):
            if two:
                nums.pop()
                nums.insert(0,2)
                two-=1
            elif one:
                nums.pop()
                nums.insert(0,1)
                one-=1
            else:
                nums.pop()
                nums.insert(0,0)
            

    