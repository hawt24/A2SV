# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
        1,first reverse 
        2,and append temporary array
        3,then count the greater using stack
        """
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        cur=prev
        temp=[]
        while cur:
            temp.append(cur.val)
            cur=cur.next
        stack=[]
        ans=[]
        for i in range(len(temp)):
            num=temp[i]
            while stack and stack[-1]<=num:
                stack.pop()
            if not stack:
                ans.append(0)
            elif stack[-1]>num:
                ans.append(stack[-1])
            stack.append(num)
        ans.reverse()
        return ans
                
                
                
                
            

        

        