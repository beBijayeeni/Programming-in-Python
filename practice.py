# initializing list
test_list = [['a' ,2], ['c' ,4], ['e' ,6]]
# printing original list
print("The original list is : ",test_list)
# Convert Lists of List to Dictionary
# Using loop
res = dict()
for sub in test_list:
    res[tuple(sub[:1])] =tuple(sub[1:])
modified_dict = {}
for key, value in res.items():
    modified_key = ''.join(key)  # Convert key tuple to string
    modified_value = value[0]  # Get the first element from the value tuple
    modified_dict[modified_key] = modified_value

# Printing the modified dictionary
print("The modified dictionary: ", modified_dict)