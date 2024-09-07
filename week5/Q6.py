import numpy as np

# Function to sort by second row
def sort_by_second_row(arr):
    return arr[:, arr[1, :].argsort()]

# Function to sort by second column
def sort_by_second_column(arr):
    return arr[arr[:, 1].argsort()]

# Create a numpy array
arr = np.array([[1, 4, 3],
                [9, 2, 6],
                [5, 7, 8]])

print("Original Array:\n", arr)

# Case 1: Sort by second row
sorted_by_second_row = sort_by_second_row(arr)
print("Sorted by second row:\n", sorted_by_second_row)

# Case 2: Sort by second column
sorted_by_second_column = sort_by_second_column(arr)
print("Sorted by second column:\n", sorted_by_second_column)

