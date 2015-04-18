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


def print_linked_list(head):
    while head:
        print str(head.val) + ' ->',
        head = head.next
    print


def get_tail(head):
    tail = head
    while tail.next:
        tail = tail.next
    return tail


def reverse_linked_list(head):
    curr, prev = head, None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev
    return head


def main():
    list = LinkedList(0)
    list_tail = get_tail(list.head)
    for i in range(1, 10):
        list.insert_after(list_tail, i)
        list_tail = list_tail.next

    head = list.head
    print_linked_list(head)

    new_head = reverse_linked_list(head)
    print_linked_list(new_head)


if __name__ == '__main__':
    main()
