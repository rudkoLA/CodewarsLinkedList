from preloaded import Node

def get_nth(node, index):
    if index < 0:
        raise IndexError

    for _ in range(index):
        if node is None:
            raise IndexError

        node = node.next

    return node
