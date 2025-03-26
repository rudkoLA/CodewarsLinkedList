def linked_list_from_string(s):
    data = s.split(' -> ')

    if " -> " not in s or not data:
        return None

    head = Node(data[0])

    for item in data:
        head = Node(item, head)

    return head