#to implement the stack using the lists in the python
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        self.stack.pop()
    def top(self):
        if len(self.stack)==0:
            return "stack empty"
        else:
            return self.stack[-1]
    def isempty(self):
        return len(self.stack)==0
    def display(self):
        return self.stack
obj=Stack()
obj.push(10)
obj.push(20)
obj.pop()
print(obj.top())
print(obj.isempty())
print(obj.display())

# to implement the stacks usiing the linkedlist in the python
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
            return
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new
        return self.head
    def pop(self):
        curr=self.head
        if self.head==None:
            return "stack is empty"
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            curr.next=None
        return curr
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="-->")
            temp=temp.next
        print(None)
obj1=linkedlist()
obj1.insert(10)
obj1.insert(20)
obj1.insert(30)
obj1.pop()
obj1.display()
