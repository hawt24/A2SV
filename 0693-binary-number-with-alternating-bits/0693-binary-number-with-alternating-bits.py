class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # if n==1:
        #     return True
        # temp=[]
        # while n:
        #     temp.append(n%2)
        #     n=n//2
        # temp[::-1]
        # for i in range(len(temp)-1):
        #     if  temp[i]==temp[i+1]:
        #         return False
        # return True
        
        temp= n&1
        n>>=1
        while n:
            if n&1==temp:
                return False
            temp=n&1
            n >>= 1
        return True
            
            
