from collections import deque
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def builder(self,arr):
        root=node(arr[0])
        queue=deque([root])
        i=1
        while i<len(arr):
            treenode=queue.popleft()
            if i<len(arr):
                treenode.left=node(arr[i])
                queue.append(treenode.left)
                i+=1
            if i<len(arr):
                treenode.right=node(arr[i])
                queue.append(treenode.right)
                i+=1
        return root





arr=[1,2,3,4,5,6]
obj=tree()
h1=obj.builder(arr)
