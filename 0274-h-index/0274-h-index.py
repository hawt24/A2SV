class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        i = 0
        for i,val in enumerate(citations):
            if i >=val:
                return i
        return i+1
