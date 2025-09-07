# To delete the node in the linkedlist we should do the following:

# 10 -> 20 -> 30 -> 40 -> 50 -> None

# I want to delete the node 30 then:
# we must do the following now:


def node(self,node):    #let my node be 30 then  copy the value to the previous node and then delete it 
    self.data=self.next.data
    self.next=self.next.next