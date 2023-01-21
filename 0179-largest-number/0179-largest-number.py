class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(n1,n2):
            if n1+n2>n2+n1:
                return 1
            elif n1==n2:
                return 0
            else:
                return -1
        #change to string
        nums=[str(num) for num in nums]
        #by using (comp) function compare and sort
        nums.sort(key = cmp_to_key(comp), reverse = True)
        
        return str(int("".join(nums))) #using int for remove leading 0's
        
        
    
        