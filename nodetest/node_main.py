class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class Solution:
    def __init__(self):
        self.tail = None

    def insert(self, head, data):
        if head is None:
            head = Node(data)
            self.tail = head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head

    @staticmethod
    def display(head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next


mylist = Solution()
T = int(input("Entry number of nodes: "))
head_node = None
for i in range(T):
    data_node = int(input(f"Set data for {i + 1} node: "))
    head_node = mylist.insert(head_node, data_node)
mylist.display(head_node)
