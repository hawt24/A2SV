# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr_1=head
        ptr_2=head.next
        temp_head=ptr_2
        while ptr_1 and ptr_1.next and ptr_2 and ptr_2.next :
            ptr_1.next=ptr_1.next.next
            ptr_2.next=ptr_2.next.next
            ptr_1=ptr_1.next
            ptr_2=ptr_2.next
        ptr_1.next=temp_head
        return head
        
        
       
     
        
        
        
    
        
            