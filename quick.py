# Python program for implementation of Quicksort Sort
def partition(array, low, high):
	pivot = array[high]

	
	i = low - 1

	
	for j in range(low, high):
		if array[j] <= pivot:

			
			i = i + 1

			
			(array[i], array[j]) = (array[j], array[i])

	
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	
	return i + 1




def quickSort(array, low, high):
	if low < high:

		
		pi = partition(array, low, high)

		quickSort(array, low, pi - 1)

		
		quickSort(array, pi + 1, high)


data=[]
n = int (input ("Enter number of elements: ")) 

# Declare an empty list
data = []

# Iterate for n times take inputs
for i in range (n):
    # Take input of ith element as x.
    x = int(input())
    # Append 'x' to the list.
    list.append(x)

# Print the list
print("Unsorted List:", list)
size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)