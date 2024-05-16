# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lo = head
        hi = head
        while hi and hi.next:
            lo = lo.next
            hi = hi.next.next
            if lo == hi:
                break
        if not hi or not hi.next:
            return None

        hi = head
        while lo != hi:
            lo = lo.next
            hi = hi.next
        return lo
