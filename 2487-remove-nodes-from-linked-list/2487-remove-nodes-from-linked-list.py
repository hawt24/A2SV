# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt 
        dummy=ListNode(0)
        temp=dummy
        temp.next=ListNode(prev.val)
        temp=temp.next
        prev=prev.next
        while prev:
            if temp.val<=prev.val:
                temp.next=ListNode(prev.val)
                temp=temp.next
            prev=prev.next
        curr=dummy.next
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    
                
            
            
            
                
                
                
            
                
    
            