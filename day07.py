class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Cannot pop from empty queue")
        return self.s1.pop()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(7)
    q.enqueue(-11)
    q.enqueue(8)
    for _ in range(4):
        q.dequeue()
    #print(q.dequeue())


