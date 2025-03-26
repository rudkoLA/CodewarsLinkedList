def linked_list_from_string(s):
    data = list(reversed(s.split(' -> ')))

    if " -> " not in s or not data:
        return None

    head = None

    data.pop(0)

    for item in data:
        head = Node(item, head)

    return head