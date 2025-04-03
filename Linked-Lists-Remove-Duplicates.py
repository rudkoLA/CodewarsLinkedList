class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    prev = head
    current = head.next

    while prev is not None and current is not None:
        if prev.data == current.data:
            prev.next = current.next
            current = current.next
        else:
            prev = prev.next
            current = current.next

    return head
