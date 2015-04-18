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


def get_nth_to_last_node(head, n):
    if n <= 0:
        return None

    fast, slow = head, head
    for _ in range(n):
        fast = fast.next
        if fast is None:
            return None

    while fast:
        fast, slow = fast.next, slow.next

    return slow


def main():
    list = LinkedList(0)
    list_tail = get_tail(list.head)
    for i in range(1, 10):
        list.insert_after(list_tail, i)
        list_tail = list_tail.next

    print_linked_list(list.head)

    new_head = reverse_linked_list(list.head)
    list.head = new_head
    print_linked_list(list.head)

    _5th_to_end = get_nth_to_last_node(new_head, 5)
    print _5th_to_end.val

    list.remove_after(_5th_to_end)
    print_linked_list(list.head)


if __name__ == '__main__':
    main()
