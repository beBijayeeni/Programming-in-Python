#Author:<Bijayeeni Halder>
#Assignment Name:<Lab Assignment 5>
#Roll No:<30001221025>
#Python Version:<3.10.5>
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.after = None
class SinglyLinkedList:
    def __init__(self):
       self.head=None
    def reverse(self):
        before=None
        current=self.head
        while(current is not None):
            after=current.after
            current.after=before
            before=current
            current=after
            self.head=before   
    def push(self,new_data):
      new_node=Node(new_data)
      new_node.after=self.head
      self.head=new_node
    def listprint(self):
      printval=self.head
      while printval is not None:
         print(printval.dataval)
         printval=printval.after

MyList=SinglyLinkedList()
MyList.push(1)
MyList.push(2)
MyList.push(3)
MyList.push(4)

print("My Original Singly Linked List is:")
MyList.listprint()
MyList.reverse()
print("\n Reversed Singly Linked List is:")
MyList.listprint()
            
