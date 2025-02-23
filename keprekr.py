import math
n=int(input("Enter a number:"))
c=0
sq=n*n
num=sq
while(sq>0):
    c+=1
    sq=sq//10
x=c//2
m=num//math.pow(10,x)
p=num%math.pow(10,x)
sum=m+p
if(sum==n):
    print("Kepreker Number")
else:
    print("Not Kepreker Number")
