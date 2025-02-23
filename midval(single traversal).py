#Author:<Bijayeeni Halder>
#Assignment Name:<Lab Assignment 4>
#Roll No:<30001221025>
#Python Version:<3.10.5>
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

   def printMiddle(self):
        slow_ptr = self.headval
        fast_ptr = self.headval
 
        if self.headval is not None:
            while (fast_ptr is not None and fast_ptr.nextval is not None):
                fast_ptr = fast_ptr.nextval.nextval
                slow_ptr = slow_ptr.nextval
            print("The middle element is: ", slow_ptr.dataval)
 
        
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.listprint()
list.printMiddle()
