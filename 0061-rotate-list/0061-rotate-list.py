# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        len_=1
        last_num=head
        while last_num.next:
            last_num=last_num.next
            len_+=1
        curr=head
        k=k%len_
        if k==0:
            return head
        for i in range(len_-k-1):
            curr=curr.next
        NewVal=curr.next
        curr.next=None
        last_num.next=head
        return NewVal
            
        
    
            