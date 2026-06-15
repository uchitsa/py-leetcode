# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        one = head
        two = head.next.next

        while two and two.next:
            one = one.next
            two = two.next.next
        one.next = one.next.next
        return head
