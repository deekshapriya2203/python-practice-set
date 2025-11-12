class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue: Add element to the queue
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    # Dequeue: Remove element from the queue
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
        elif self.front == self.rear:
            print(f"Deleted element: {self.queue[self.front]}")
            self.front = -1
            self.rear = -1
        else:
            print(f"Deleted element: {self.queue[self.front]}")
            self.front = (self.front + 1) % self.size

    # Display: Show elements of the queue
    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return
        print("Circular Queue Elements:")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
cq.dequeue()
cq.enqueue(50)
cq.display()
cq.enqueue(60)  