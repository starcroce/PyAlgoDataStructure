import MyDoubleLinkedList


class DoubleLinkedListStack:

    def __init__(self):
        self.front = None
        self.rear = None
        self.content = None

    def push(self, val):
        # push to empty queue
        if self.content is None:
            self.content = MyDoubleLinkedList.LinkedList(val)
            self.front = self.content.head
            self.rear = self.content.tail
        else:
            self.content.insert_before(self.content.head, val)
            self.front = self.content.head

    def pop(self):
        if self.is_empty() is True:
            print 'Pop from empty queue'
            return
        self.content.remove(self.rear)
        self.rear = self.content.tail

    def is_empty(self):
        return self.content is None

    def print_queue(self):
        if self.is_empty():
            print 'None'
        else:
            curr = self.front
            while curr != self.rear:
                print str(curr.val) + ' ->',
                curr = curr.next
            print str(curr.val)


def main():
    my_queue = DoubleLinkedListStack()
    my_queue.print_queue()

    for i in range(10):
        my_queue.push(i)
    my_queue.print_queue()

    for i in range(5):
        my_queue.pop()
    my_queue.print_queue()


if __name__ == '__main__':
    main()
