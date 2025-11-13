class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 🔁 Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # store next node
            current.next = prev        # reverse the link
            prev = current             # move prev forward
            current = next_node        # move current forward
        self.head = prev               # reset head to last node

# Example Usage
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

print("Original Linked List:")
ll.display()

ll.reverse()
print("Reversed Linked List:")
ll.display()
