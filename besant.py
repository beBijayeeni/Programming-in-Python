# Taking input from the user for the number
number = int(input("Enter a number: "))

# Initialize a variable to store the count of digits
count = 0

# Counting the number of digits
while number > 0:
    # Increment the count for each digit
    count += 1
    
    # Remove the last digit from the number
    number //= 10

# Displaying the count of digits
print("Number of digits:", count)
