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
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 🧩 Find middle element
    def find_middle(self):
        slow = self.head
        fast = self.head
        if self.head is None:
            print("The list is empty.")
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle element is:", slow.data)

# Example usage
ll = LinkedList()
for value in [10, 20, 30, 40, 50]:
    ll.insert_at_end(value)

print("Linked List:")
ll.display()
ll.find_middle()
