def loop_size(node):
    tortoise = node
    hare = node.next

    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next

    count = 1
    current = tortoise.next

    while current != tortoise:
        current = current.next
        count += 1

    return count
