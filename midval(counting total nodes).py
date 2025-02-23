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

   def getlen(self):
        n=self.headval
        length=0
        while(n!=None):
            length+=1
            n=n.nextval
        return length    
   def midval(self):
        n=self.headval
        len=self.getlen()
        for i in range(len//2):
            n=n.nextval
        print()    
        print("The middle value is ",n.dataval)
        
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.listprint()
list.midval()
