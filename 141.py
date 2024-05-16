# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lo = head
        hi = head
        while hi and hi.next:
            lo = lo.next
            hi = hi.next.next
            if lo == hi:
                return True
        if not hi or not hi.next:
            return False
