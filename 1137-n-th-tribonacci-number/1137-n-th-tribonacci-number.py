class Solution:
    def __init__(self):
        self.memo={}
    def tribonacci(self, num: int) -> int:

        if num==0:
            return 0
        if num==1:
            return 1
        if num==2:
            return 1
        if num not in self.memo:
            self.memo[num]=self.tribonacci(num-1)+self.tribonacci(num-2)+self.tribonacci(num-3)
        return self.memo[num]
                
            
        