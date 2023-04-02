# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1=""
        L2=""
        
        curr=l1
        while curr:
            L1+=str(curr.val)
            curr=curr.next
        
        curr=l2
        while curr:
            L2+=str(curr.val)
            curr=curr.next
     
        L_1=int(L1[::-1])
        L_2=int(L2[::-1])
        
        temp=str(L_1+L_2)
        print(temp)
        
        head = None
        for i in temp:
            val= ListNode(i)
            val.next = head
            head = val
        return head