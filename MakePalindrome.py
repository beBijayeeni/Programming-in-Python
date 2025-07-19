def min(s1,s2):
    c = 0
    rev_s1 = s1[::-1]
    rev_s2 = s2[::-1]
    for i in range(len(rev_s1)):
        if(rev_s1[i]!=rev_s2[i]):
                c += 1
    print(c)
s1 = "hello" #olleh
s2 = "world" #dlrow
min(s1,s2)
