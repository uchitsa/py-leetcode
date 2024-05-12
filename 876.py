class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    onex = head
    twox = head
    while twox and twox.next:
        onex = onex.next
        twox = twox.next.next
    return onex
