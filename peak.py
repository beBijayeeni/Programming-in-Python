r = [6523,6613,6719,6845,6813,6752,6703,6527]
max = 0
j = 0 
for i in range(0,8):
    if(r[i]>max):
        max = r[i]
        j = i
print(max)
print(j)
t=3*0.5*j 
print(t)
