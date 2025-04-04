def loop_size(node):
    all_nodes = []

    while node not in all_nodes:
        all_nodes.append(node)
        node = node.next

    all_nodes = []

    while node not in all_nodes:
        all_nodes.append(node)
        node = node.next

    return len(all_nodes)
