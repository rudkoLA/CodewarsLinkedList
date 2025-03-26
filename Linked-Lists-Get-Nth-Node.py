from preloaded import Node

def get_nth(node, index):
    for _ in range(index):
        if node is None:
            raise IndexError

        node = node.next

    return node
