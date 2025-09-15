class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=node(1)
root.left=node(2)
root.left.left=node(3)
root.left.right=node(4)

root.right=node(5)
root.right.right=node(6)

def iot(root):
    if root==None:
        return 
    
    print(root.data,end=" ")
    iot(root.left)
    iot(root.right)
iot(root)