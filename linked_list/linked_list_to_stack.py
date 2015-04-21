import MySingleLinkedList


class LinkedListStack:

    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = MySingleLinkedList.ListNode(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        res = self.top
        self.top = self.top.next
        return res

    def is_empty(self):
        return self.top == None

    def print_stack(self):
        if self.is_empty():
            print 'None'
        else:
            curr = self.top
            while curr:
                print str(curr.val) + ' ->',
                curr = curr.next
            print


def main():
    my_stack = LinkedListStack()
    my_stack.print_stack()

    for i in range(5):
        my_stack.push(i)
    my_stack.print_stack()

    popped_node = my_stack.pop()
    print popped_node.val
    my_stack.print_stack()


if __name__ == '__main__':
    main()
