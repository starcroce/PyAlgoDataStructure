import MyDoubleLinkedList

class DoubleLinkedListStack:

    def __init__(self):
        self.front = None
        self.rear = None
        self.content = None

    def push(self, val):
        if self.content is None:
            self.content = MyDoubleLinkedList.LinkedList(val)
            self.front = self.content.head
            self.rear = self.content.tail
        else:
            self.content.insert_before(self.content.head, val)