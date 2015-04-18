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


def main():
    # create a new linked list
    list = MySingleLinkedList.LinkedList(0)
    list_tail = list.get_tail()
    for i in range(1, 10):
        list.insert_after(list_tail, i)
        list_tail = list_tail.next
    list.print_list()

    print is_circle(list)

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
