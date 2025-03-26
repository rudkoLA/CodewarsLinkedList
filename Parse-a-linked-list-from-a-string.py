def linked_list_from_string(s):
    data = s.split(' -> ')[::-1]

    if " -> " not in s or not data:
        return None

    data.pop(0)
    data = map(lambda x: int(x) if x.strip().isnumeric() else x, data)
    head = None

    for item in data:
        head = Node(item, head)

    return head