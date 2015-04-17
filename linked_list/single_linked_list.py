class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, val):
        self.head = ListNode(val)
        self.tail = self.head

    def add(self, val):
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next


def print_linked_list(head):
    while head:
        print str(head.val) + ' ->',
        head = head.next
    print


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
    linked_list = LinkedList(0)
    for i in range(1, 10):
        linked_list.add(i)

    head = linked_list.head
    print_linked_list(head)

    new_head = reverse_linked_list(head)
    print_linked_list(new_head)


if __name__ == '__main__':
    main()
