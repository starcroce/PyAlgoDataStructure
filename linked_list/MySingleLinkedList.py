class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, val):
        self.head = ListNode(val)

    def insert_after(self, node, val):
        next_node = node.next
        new_node = ListNode(val)
        node.next = new_node
        new_node.next = next_node

    def remove_after(self, node):
        to_remove_node = node.next
        new_next_node = to_remove_node.next
        node.next = new_next_node

    def print_list(self):
        curr = self.head
        while curr:
            print str(curr.val) + ' ->',
            curr = curr.next
        print

    def get_tail(self):
        tail = self.head
        while tail.next:
            tail = tail.next
        return tail
