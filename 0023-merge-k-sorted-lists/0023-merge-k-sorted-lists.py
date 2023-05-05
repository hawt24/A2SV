# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=ListNode()
        dummy=ans
        
        heap=[]
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap,(lists[i].val,i))
        while heap:
            value,i=heappop(heap)
            ans.next=ListNode(value)
            ans=ans.next
            
            lists[i]=lists[i].next
            
            if lists[i]:
                heappush(heap,(lists[i].val,i))
                
        return dummy.next
            
                
        
                
        
                
        
        