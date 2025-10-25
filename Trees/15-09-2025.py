# class node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# root=node(1)
# root.left=node(2)
# root.left.left=node(3)
# root.left.right=node(4)

# root.right=node(5)
# root.right.right=node(6)

# def iot(root):
#     if root==None:
#         return 
    
#     print(root.data,end=" ")
#     iot(root.left)
#     iot(root.right)
# iot(root)

# the problem to perform the Inorder traversal :
# that is first the left,root,right......
# we use the Recursion for this:

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def iot(self,root):
        if root==None:
            return 
   
        print(root.data,end=" ")
        self.iot(root.left)
        self.iot(root.right)


root=node(1)
root.left=node(2)
root.left.left=node(3)
root.left.right=node(4)
root.right=node(5)
root.right.right=node(6)



print("Inorder: ",end=" "); iot(root); print()



# def Iot(self,root,list1):
#     Iot(root.left,list1)
#     list1.append(root.data)
#     Iot(root.right,list1)

# def mainfun(self,root):
#     list1=[]
#     Iot(root,list1)
#     return list1

# root=node(1)
# root.left=node(2)
# root.left.left=node(3)
# root.left.right=node(4)
# root.right=node(5)
# root.right.right=node(6)
# print(mainfun(root))


# a=[1,1,2,2,3,4]
# dici={}
# for i in a:
#     print(dici.get(i,0))
#     dici[i]=dici.get(i,0)+1
#     print(dici)