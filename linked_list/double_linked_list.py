import MyDoubleLinkedList


def find_nth_node(list, n):
    curr = list.head
    for _ in range(n):
        curr = curr.next
    return curr


def main():
    double_list = MyDoubleLinkedList.LinkedList(0)
    for i in range(1, 10):
        double_list.insert_after(double_list.tail, i)

    double_list.print_list()

    _3rd_node = find_nth_node(double_list, 3)
    print _3rd_node.val, _3rd_node.prev, _3rd_node.next.val

    double_list.insert_after(_3rd_node, 100)
    double_list.print_list()

    print _3rd_node.val, _3rd_node.prev#, _3rd_node.next.val

    # double_list.remove(_3rd_node)
    # double_list.print_list()

if __name__ == '__main__':
    main()
