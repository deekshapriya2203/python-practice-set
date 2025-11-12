class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # Push an element onto the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto the stack")

    # Pop the top element
    def pop(self):
        if self.top is None:
            print("Stack Underflow! Cannot pop.")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f"Popped element: {popped}")

    # Peek at the top element
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(f"Top element: {self.top.data}")

    # Display all elements
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp = self.top
        print("Stack elements are:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
