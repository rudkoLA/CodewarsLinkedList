class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    first = head
    second = head.next

    last_first = first
    last_second = second

    if head.next.next is None:
        first.next = None
        return Context(first, second)

    switch = True

    head = head.next.next

    while head is not None:
        if switch:
            last_first.next = head
            last_first = last_first.next
        else:
            last_second.next = head
            last_second = last_second.next

        head = head.next
        switch = not switch

    last_first.next = None
    last_second.next = None

    return Context(first, second)
