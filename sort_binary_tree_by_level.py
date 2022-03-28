# Your task is to return the list with elements from node sorted by levels, which means the current element goes first,
# then current children (from left to right) are second and third, and so on.
#
# Return empty list if current is None.
#
# Example 1 - following node:
#
#                  2
#             8        9
#           1  3     4   5
#
# Should return following list:
#
# [2,8,9,1,3,4,5]
#
# Example 2 - following node:
#
#                  1
#             8        4
#               3        5
#                          7
#
# Should return following list:
#
# [1,8,4,3,5,7]

class Node:
    def __init__(self, n, left, right):
        self.left = left
        self.right = right
        self.value = n


def show_nods_numbers(node):
    node_value = list()
    checked = []
    checked.append(node)
    level = 0
    print(f"Tree level is: {level}", checked)

    while checked:
        level += 1
        current = checked.pop()
        node_value.append(current.value)

        if current.left is not None:
            checked.append(current.left)

        if current.right is not None:
            checked.append(current.right)

    return node_value


tree = Node(1, None, None)
print(show_nods_numbers(tree))