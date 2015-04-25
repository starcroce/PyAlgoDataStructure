class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self, val):
        self.head = ListNode(val)
        self.tail = self.head

    def insert(self, prev_node, next_node, val):
        new_node = ListNode(val)
        new_node.prev, new_node.next = prev_node, next_node
        prev_node.next = new_node
        next_node.prev = new_node

    def insert_after(self, node, val):
        next_node = node.next
        if next_node is None:
            node.next = ListNode(val)
            self.tail = node.next
        else:
            self.insert(node, next_node, val)

    def insert_before(self, node, val):
        prev_node = node.prev
        if prev_node is None:
            node.prev = ListNode(val)
            self.tail = node.prev
        else:
            self.insert(prev_node, node, val)

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
