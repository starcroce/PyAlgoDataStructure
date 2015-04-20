import MySingleLinkedList


def reverse_linked_list(list):
    curr, prev = list.head, None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev
    list.head = head


def get_nth_to_last_node(list, n):
    if n <= 0:
        return None
    fast, slow = list.head, list.head
    for _ in range(n):
        fast = fast.next
        if fast is None:
            return None
    while fast:
        fast, slow = fast.next, slow.next
    return slow


def is_circle(list):
    fast, slow = list.head, list.head
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is None or fast.next is None:
            return False
        if fast is slow:
            return True


def get_circle_start(list):
    fast, slow = list.head, list.head
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    fast = list.head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


def find_nth_node(list, n):
    res = list.head
    for _ in range(n - 1):
        res = res.next
        if res is None:
            return None
    return res


def swap_two_nodes(list, node1, node2):
    before_node1, before_node2 = list.head, list.head
    while before_node1.next != node1:
        before_node1 = before_node1.next
    while before_node2.next != node2:
        before_node2 = before_node2.next
    after_node1, after_node2 = node1.next, node2.next
    before_node1.next = node2
    node2.next = after_node1
    before_node2.next = node1
    node1.next = after_node2


def main():
    # create a new linked list
    list = MySingleLinkedList.LinkedList(0)
    list_tail = list.get_tail()
    for i in range(1, 10):
        list.insert_after(list_tail, i)
        list_tail = list_tail.next
    list.print_list()

    print is_circle(list)

    _3rd_node, _6th_node = find_nth_node(list, 3), find_nth_node(list, 6)
    print _3rd_node.val, _6th_node.val
    swap_two_nodes(list, _3rd_node, _6th_node)
    list.print_list()

    # find 5th to the end node and remove it
    _5th_to_end = get_nth_to_last_node(list, 5)
    print _5th_to_end.val
    list.remove_after(_5th_to_end)
    list.print_list()

    # reverse linked list
    reverse_linked_list(list)
    list.print_list()

    # create an linked list circle
    new_tail = list.get_tail()
    _5th_to_end = get_nth_to_last_node(list, 5)
    new_tail.next = _5th_to_end

    print is_circle(list)
    circle_start = get_circle_start(list)
    print circle_start.val, _5th_to_end.val


if __name__ == '__main__':
    main()
