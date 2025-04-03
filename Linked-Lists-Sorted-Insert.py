def sorted_insert(head, data):
    if head.data >= data:
        mid_node = Node(data)
        mid_node.next = head

        return mid_node

    head.next = sorted_insert(head.next, data)

    return head
