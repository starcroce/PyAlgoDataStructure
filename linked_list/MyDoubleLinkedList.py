class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self, val):
        self.head = ListNode(val)
        self.tail = self.head

    def insert(self, prev_node, new_node, next_node):
        new_node.prev = prev_node
        prev_node.next = new_node
        new_node.next = next_node
        next_node.prev = new_node

    def insert_after(self, node, val):
        new_node = ListNode(val)
        next_node = node.next
        if next_node is None:
            node.next = new_node
            new_node.prev = node
            self.tail = new_node
        else:
            self.insert(node, new_node, next_node)

    def insert_before(self, node, val):
        new_node = ListNode(val)
        prev_node = node.prev
        if prev_node is None:
            node.prev = new_node
            new_node.next = node
            self.head = new_node
        else:
            self.insert(prev_node, new_node, node)

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def print_list(self):
        curr = self.head
        while curr:
            print '<-' + str(curr.val) + '->',
            curr = curr.next
        print
