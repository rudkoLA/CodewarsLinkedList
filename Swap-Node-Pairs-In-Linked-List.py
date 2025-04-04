class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None:
        return None

    if head.next is None:
        return head

    root = head.next

    prev = None
    current = head

    while current and current.next:
        rest = current.next.next
        temp = current.next

        temp.next = current
        current.next = rest

        if prev is not None:
            prev.next = temp

        prev = current
        current = rest

    return root
