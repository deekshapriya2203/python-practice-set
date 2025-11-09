class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Function to insert a new key
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # Function for inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

# Example usage
bst = BST()
root = None
for key in [50, 30, 20, 40, 70, 60, 80]:
    root = bst.insert(root, key)

print("Inorder traversal of BST:", end=" ")
bst.inorder(root)
