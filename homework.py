import math
n=int(input("Enter a number:"))
c=0
s=0
num=n
while(n>0):
    c+=1
    n=n//10
b=num
while(num>0):
    a=num%10
    s=s+math.pow(a,c)
    num=num//10
    c-=1
if(s==b):
    print("Disarium Number")
else:
    print("Not Disrium Number")