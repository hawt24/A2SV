# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        first store in list then sort after sorting convert to linked list
        """
        temp=[]
        curr=head
        while curr:
            temp.append(curr.val)
            curr=curr.next
        temp.sort()
        
        dummy=ListNode()
        val=dummy
        for i in temp:
            val.next=ListNode(i)
            val=val.next
        return dummy.next
            
        
        