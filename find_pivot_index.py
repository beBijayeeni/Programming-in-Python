def find_pivot_index(N, arr):
    min_val = float('inf')
    pivot_index = -1

    for i in range(N):
        if arr[i] != -1:
            if arr[i] < min_val:
                min_val = arr[i]
                pivot_index = i

    print(pivot_index)

# --- Input Reading ---
N = int(input('Enter the no. of elements: '))
print('Enter the elements:')

# Read N elements, each on a new line
arr = []
for i in range(N):
    arr.append(int(input())) # Read each number as an integer

# Call the function
find_pivot_index(N, arr)
