# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        using two pointers and update one with a delay of <n> steps.
        '''
        fast=head
        for i in range(n): #for knowing by how much faster than slower 
            fast=fast.next
        if fast is None:  #but this if stetment we can remove using dummy node
            return head.next

        slow=head
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
            
        