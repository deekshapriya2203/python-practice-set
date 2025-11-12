class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1️⃣ Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2️⃣ Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 3️⃣ Insert after a given node
    def insert_after(self, prev_node_data, data):
        temp = self.head
        while temp and temp.data != prev_node_data:
            temp = temp.next
        if not temp:
            print("Previous node not found!")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # 4️⃣ Delete a node by key
    def delete_node(self, key):
        temp = self.head

        # If head node holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key not found
        if not temp:
            print("Node not found!")
            return

        prev.next = temp.next
        temp = None

    # 5️⃣ Display the list
    def display(self):
        temp = self.head
        if not temp:
            print("Lis
