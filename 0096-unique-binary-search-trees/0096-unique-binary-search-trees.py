class Solution:
    def numTrees(self, n: int) -> int:
        arr=[1]*(n+1)
        ans=0
        for i in range(2,n+1):
            catalan=0
            for j in range(1,i+1):
                left=j-1
                right=i-j
                catalan+=arr[left]*arr[right]
            arr[i]=catalan
        return arr[n]
        

        
        