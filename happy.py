def Happy(x):
    s=0
    while(s!=1 and s!=4):
        s=0
        while(x>0):
            a=x%10
            s=s+a
            x=x//10
    return s
num1=int(input("Enter number:"))
p=Happy(num1)
if(p==1):
    print("The number is niven")
else:
    print("The number is not niven")
