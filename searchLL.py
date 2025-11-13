class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        position = 1
        while current:
            if current.data == key:
                return f"Element {key} found at position {position}"
            current = current.next
            position += 1
        return f"Element {key} not found in the list"

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
for val in [5, 10, 15, 20, 25]:
    ll.append(val)

print("Linked List:")
ll.display()

# Searching elements
print(ll.search(15))
print(ll.search(40))
