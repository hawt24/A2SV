#User function Template for python3
import heapq
from heapq import heappush,heappop

class Solution:
    #Heapify function to maintain heap property.
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        heap = [arr[0]]
        for val in arr[1:]:
           heappush(heap,val)
        result = []
        # print(heap)
        c = 0
        for i in range(n):
            arr[c] = (heappop(heap))
            c += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends