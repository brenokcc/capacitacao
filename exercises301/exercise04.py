
def identify(node1, node2, node3):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {key: (node1.get(key, 0), node2.get(key, 0), node3.get(key, 0)) for key in relevant}
    return result
