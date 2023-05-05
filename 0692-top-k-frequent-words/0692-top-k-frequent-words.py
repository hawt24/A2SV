class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt=Counter(words)
        words=list(set(words))
        heap=[]
        ans=[]
        for i in range(len(words)):
            heappush(heap,[cnt[words[i]],words[i]])
            
        for i in range(len(heap)):
            heap[i][0]*=-1
    
        heapify(heap)
        while k>0:
            ans.append(heappop(heap)[1])
            k-=1
        return ans

        