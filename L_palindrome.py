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

    def is_palindrome(self):
        # Step 1: Copy all values to a list
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        
        # Step 2: Check if list equals its reverse
        return values == values[::-1]

# Example usage
ll = LinkedList()
for i in [1, 2, 3, 2, 1]:
    ll.append(i)

if ll.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
