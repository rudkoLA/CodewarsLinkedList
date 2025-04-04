class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return None

    current = head

    while current.next is not None:
        prev = current
        current = current.next

    try:
        prev.next = None
    except UnboundLocalError:
        return Node(head.data)

    new = Node(current.data)

    new.next = reverse(head)

    return new
