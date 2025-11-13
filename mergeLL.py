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
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# 🔁 Function to merge two sorted linked lists
def merge_sorted_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.data < list2.data:
        result = list1
        result.next = merge_sorted_lists(list1.next, list2)
    else:
        result = list2
        result.next = merge_sorted_lists(list1, list2.next)

    return result

# Example usage
list1 = LinkedList()
list2 = LinkedList()

for val in [10, 30, 50]:
    list1.insert_at_end(val)

for val in [20, 40, 60]:
    list2.insert_at_end(val)

print("List 1:")
list1.display()
print("List 2:")
list2.display()

# Merge both lists
merged_head = merge_sorted_lists(list1.head, list2.head)

# Display merged result
print("Merged Sorted List:")
temp = merged_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
