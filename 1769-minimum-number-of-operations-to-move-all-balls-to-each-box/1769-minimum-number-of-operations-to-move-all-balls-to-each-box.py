class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        boxes=[int(i) for i in boxes]
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if boxes[j]==1:
                    count+=abs(i-j)
            ans.append(count)
        return ans