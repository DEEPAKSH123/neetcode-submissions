# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            prev=None
            cur=head
            while cur:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            return prev

        prevSlow=None
        slow,fast=head,head
        while slow and fast:
            prevSlow=slow
            slow=slow.next
            fast=fast.next.next if fast.next else None
        
        prevSlow.next=None
        head2=reverse(slow)
        t1,t2=head,head2
        while t1 and t2:
            temp1=t1.next
            temp2=t2.next
            t1.next=t2
            t2.next=temp1
            t1=temp1
            t2=temp2


        


        