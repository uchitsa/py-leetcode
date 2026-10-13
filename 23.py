# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode()
        cur = dummy
        minheap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(minheap, (lists[i].val, i))
        while minheap:
            val, i = heappop(minheap)
            cur.next = lists[i]
            cur = cur.next

            if lists[i].next:
                lists[i] = lists[i].next
                heappush(minheap, (lists[i].val, i))
        return dummy.next
