from preloaded import Node

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def build_one_two_three():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = None

    return node_1