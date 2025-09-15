# to implement the queue using the lists
class Queue:
    def __init__(self):
        self.queue=[]
    def push(self,data):
        self.queue.append(data)
    def pop(self):
        self.queue.pop(0)
    def isempty(self):
        if len(self.queue)==0:
            return "queue is empty"
        else:
            return len(self.queue)
    def peek(self):
        if self.isempty()==0:
            return "queue is empty "
        else:
            return self.queue[0]
    def display(self):
        return self.queue

obj=Queue()
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
print(obj.peek())
print(obj.display())

#to implement the queues using the linkedlist

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        new=node(data)








        if self.head==None:
            self.head=new
            self.tail=new
        else:
            self.tail.next=new
            self.tail=new

        # else:
        #     curr=self.head
        #     while curr.next!=None:
        #         curr=curr.next
        #     curr.next=new
    def dequeue(self):
        pop=self.head.data
        self.head=self.head.next
        return pop
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    
obj=Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.display()
obj.dequeue()
obj.display()
    


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def isEmpty(self):
        return self.head==None
    def dequeue(self):
        if self.isEmpty():
            print("No elements Exist for dequeue")
        else:
            self.head=self.head.next
    def peek(self):
        if self.isEmpty():
            print("No elements Exist")
        else:
            return self.head.data
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()

print(q.peek())