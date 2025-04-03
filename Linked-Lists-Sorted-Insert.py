def sorted_insert(head, data):
    if head is None:
        return Node(data)

    if head.data >= data:
        mid_node = Node(data)
        mid_node.next = head

        return mid_node

    if head.next is None:
        new_node = Node(data)
        head.next = new_node
        return head

    head.next = sorted_insert(head.next, data)

    return head
