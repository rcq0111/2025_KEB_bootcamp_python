def a(i):
    j = 9
    print(i, j)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

def b(k):
    a(1)
    print(k)
def main():
    print("start")
    b(3)
    print("end")
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:  # if next node exist
            current = current.next  # move
        current.next = Node(data)


if __name__ == "__main__":
    main()
    l = LinkedList()
    l.append(7)
    l.append(-11)
    l.append(8)