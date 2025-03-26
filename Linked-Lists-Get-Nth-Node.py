from preloaded import Node

def get_nth(node, index):
    if index < 0 or node is None:
        raise IndexError

    for _ in range(index):
        if node.next is None:
            raise IndexError

        node = node.next

    return node
