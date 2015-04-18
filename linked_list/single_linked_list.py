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


def is_circle(head):
    fast, slow = head, head
    while True:
        fast = fast.next.next
        slow = slow.next

        if fast is None or fast.next is None:
            return False
        if fast is slow:
            return True


def get_circle_start(head):
    fast, slow = head, head
    while True:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            break
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


def main():
    # create a new linked list
    list = LinkedList(0)
    list_tail = get_tail(list.head)
    for i in range(1, 10):
        list.insert_after(list_tail, i)
        list_tail = list_tail.next
    print_linked_list(list.head)

    print is_circle(list.head)

    # find 5th to the end node and remove it
    _5th_to_end = get_nth_to_last_node(list.head, 5)
    print _5th_to_end.val
    list.remove_after(_5th_to_end)
    print_linked_list(list.head)

    # reverse linked list
    new_head = reverse_linked_list(list.head)
    list.head = new_head
    print_linked_list(list.head)

    # create an linked list circle
    new_tail = get_tail(list.head)
    _5th_to_end = get_nth_to_last_node(list.head, 5)
    new_tail.next = _5th_to_end

    print is_circle(list.head)
    circle_start = get_circle_start(list.head)
    print circle_start.val, _5th_to_end.val


if __name__ == '__main__':
    main()
