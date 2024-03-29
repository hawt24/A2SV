#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heappush(self,heap,value):
        heap.append(value)
        current = len(heap) - 1
        self.heapify_up(heap,current)
        
    def heapify_up(self,heap,curr):
        par = (curr - 1) // 2
        while curr > 0 and heap[par] > heap[curr]:
            heap[par],heap[curr] = heap[curr],heap[par]
            curr = par
            par = (curr - 1) // 2
    def heappop(self,heap):
        if not heap:
            return None
        min_value = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        current = 0
        self.heapify_down(heap,len(heap),current)
        return min_value

    def heapify_down(self,heap,length,curr):
        left = (2*curr + 1)
        right = (2*curr + 2)
        sm = 0
        if left >= length:
            return
        if right >= length and left < length:
            sm = left
        else: 
            sm = left if heap[left] < heap[right] else right
        if heap[sm] < heap[curr]:
            heap[sm],heap[curr] = heap[curr],heap[sm]
            self.heapify_down(heap,length,sm)

        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        heap = [arr[0]]
        for val in arr[1:]:
            self.heappush(heap,val)
        result = []
        # print(heap)
        for i in range(n):
            temp = self.heappop(heap)
            result.append(temp)
        c = 0
        for i in result:
            arr[c] = i
            c += 1