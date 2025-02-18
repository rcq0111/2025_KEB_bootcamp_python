
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.net = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data): # enqueue 를 하면  rear가 증가한다
        self._size += 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node # increase rear

    def dequeue(self): # dequeue를 하면 front가 증가한다.
        if self.front is None:
            raise IndexError('pop from empty queue')
        self._size  -= self._size
        temp = self.front # backup / return 용도
        self.front = self.front.next # update
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        return self._size

if __name__ == "__main__":
    q = Queue()
    #q.enqueue(7)
    #q.enqueue(-11)
    #q.enqueue(8)
    print(q.size())
    #print(q.dequeue())


