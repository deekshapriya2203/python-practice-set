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

    def delete(self, key):
        current = self.head

        # Case 1: If the element to delete is the head
        if current and current.data == key:
            self.head = current.next
            return f"{key} deleted (was head node)"

        # Case 2: Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Case 3: Not found
        if not current:
            return f"{key} not found"

        # Case 4: Node found — delete it
        prev.next = current.next
        return f"{key} deleted"

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
for num in [10, 20, 30, 40, 50]:
    ll.append(num)

print("Original List:")
ll.display()

print(ll.delete(30))
print(ll.delete(10))
print(ll.delete(100))

print("List After Deletions:")
ll.display()
