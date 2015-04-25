import MyDoubleLinkedList


def main():
    double_list = MyDoubleLinkedList.LinkedList(0)
    for i in range(1, 10):
        double_list.insert_after(double_list.tail, i)

    double_list.print_list()
    print double_list.head.val, double_list.tail.val


if __name__ == '__main__':
    main()
