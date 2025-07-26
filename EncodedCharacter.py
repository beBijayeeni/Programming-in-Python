def solve(s):
    encoded_s = ""
    for i in range(len(s)):
        if (i + 1) % 2 == 0:  # Check for odd indices
            char = s[i]
            if char.lower() == 'y':
                encoded_char = 'B'
            elif char.lower() == 'z':
                encoded_char = 'C'
            elif 'a' <= char.lower() <= 'x':
                encoded_char = chr(ord(char) + 3).upper()
            elif 'A' <= char.lower() <= 'X':
                encoded_char = chr(ord(char) + 3).upper()
            else:
                encoded_char = char # if it is not alphabet then it will remain same.
            encoded_s += encoded_char
        else:
            encoded_s += s[i]
    return encoded_s

s = input("Enter your string: ")
outcome = solve(s)
print(outcome)
