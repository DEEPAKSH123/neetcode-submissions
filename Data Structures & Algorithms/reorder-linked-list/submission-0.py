# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        cur=slow.next
        slow.next=None
        while cur:
            t=cur.next
            cur.next=prev
            prev=cur
            cur=t
        l1=head
        l2=prev
        while l2:
            a,b=l1.next,l2.next
            l1.next=l2
            l2.next=a
            l1=a
            l2=b
        

        