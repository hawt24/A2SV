#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            minm=i
            for j in range(1+i,len(arr)):
                if arr[minm]>arr[j]:
                    minm=j
            arr[minm],arr[i]=arr[i],arr[minm]
        return arr
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
