class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
       
        seieve=[0]*(right+1)
        seieve[1]=1
        seieve[0]=1

        for i in range(2,right+1):
            if seieve[i]==0:
                j=i*i
                while(j<=right):
                    seieve[j]=1
                    j+=i
        

        prime=[]
        for i in range(left,right+1):
            if seieve[i]==0:
                prime.append(i) 

        if len(prime)>=2:
            
            minm=float("inf")
            for i in range(0,len(prime)-1):
                diff=prime[i+1]-prime[i]

                if diff<minm:
                    minm=diff
                    ans=[prime[i],prime[i+1]]
            return ans
        else:
            return [-1,-1]
    
                
        
        