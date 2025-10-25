# To delete the node in the linkedlist we should do the following:

# 10 -> 20 -> 30 -> 40 -> 50 -> None

# I want to delete the node 30 then:
# we must do the following now:


# def node(self,node):    #let my node be 30 then  copy the value to the previous node and then delete it 
#     self.data=self.next.data
#     self.next=self.next.next


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked:
    def createinput(self,values):
        head=node(values[0])
        curr=head
        for val in values[1:]:
            curr.next=node(val)
            curr=curr.next
        curr.next=head
        return head
    def display(self,h1):
        temp=h1
        print(temp.data,end="-->")
        temp=temp.next
        a=[]
        while temp!=h1:
            temp=temp.next
            a.append(temp.data)
            temp=temp.next
        return a
            
        




values=[1,2,3,4,5,6]
obj=Linked()
h1=obj.createinput(values)
print(obj.display(h1))
