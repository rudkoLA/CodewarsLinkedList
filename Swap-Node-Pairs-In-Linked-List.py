class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head:
        return head

    root = head.next

    prev = None
    current = head

    while current and current.next:
        rest = current.next.next
        temp = current.next

        temp.next = current
        current.next = rest

        prev.next = temp

        prev = current
        current = rest

    return root
