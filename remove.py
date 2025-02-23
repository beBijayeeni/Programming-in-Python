
li=eval(input("enter the list:"))
ele=int(input("enter the element to remove"))
li2=[]
for i in range(0,len(li)):
    if(li[i]==ele):
        k=i
        print(k)
for j in range(k,len(li)-1):
    li[j]=li[j+1]
    li=li[:len(li)-1]
    print(li)
