class binarytree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def insert(self,root,data):
        if root.data==None:
            root.data=data
        else:
            if data >=root.data:
                if root.right:
                    root.insert(root.right,data)
                else:
                    root.right=binarytree(data)
            else:
                if root.left:
                    root.insert(root.left,data)
                else:
                    root.left=binarytree(data)
    def inorder(self,root):
        if root:
            root.inorder(root.left)
            print(root.data)
            root.inorder(root.right)

root=binarytree(None)
while True:
    opt=int(input("enter your option"))
    if opt==1:
        l=int(input("length"))
        for i in range(l):
            ele=int(input("data: "))
            root.insert(root,ele)
    elif opt==2:
        root.inorder(root)
    else:
        print("tq")
        break
    
