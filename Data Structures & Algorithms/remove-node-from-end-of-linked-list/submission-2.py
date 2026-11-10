# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        dummy=ListNode(0)
        cur=head
        temp=dummy
        dummy.next=head

        while n and cur:
            n-=1
            cur=cur.next
        if cur:
            temp=temp.next
        while cur and cur.next:
            cur=cur.next
            temp=temp.next
        temp.next=temp.next.next
        return dummy.next

