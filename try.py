try:
    num = int(input("Enter a number: "))
    assert num>9
except:
    print("not a double digit number!")
else:
    reciprocal = num*5
    print(reciprocal)