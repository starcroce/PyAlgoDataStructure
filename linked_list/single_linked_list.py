import MySingleLinkedList


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
    list = MySingleLinkedList.LinkedList(0)
    list_tail = list.get_tail()
    for i in range(1, 10):
        list.insert_after(list_tail, i)
        list_tail = list_tail.next
    list.print_list()

    print is_circle(list.head)

    # find 5th to the end node and remove it
    _5th_to_end = get_nth_to_last_node(list.head, 5)
    print _5th_to_end.val
    list.remove_after(_5th_to_end)
    list.print_list()

    # reverse linked list
    new_head = reverse_linked_list(list.head)
    list.head = new_head
    list.print_list()

    # create an linked list circle
    new_tail = list.get_tail()
    _5th_to_end = get_nth_to_last_node(list.head, 5)
    new_tail.next = _5th_to_end

    print is_circle(list.head)
    circle_start = get_circle_start(list.head)
    print circle_start.val, _5th_to_end.val


if __name__ == '__main__':
    main()
