import numpy as np

def odd_rows_even_columns(arr):
    return arr[1::2, ::2]  # Odd rows and even columns

# Create a numpy array
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Odd rows and even columns:\n", odd_rows_even_columns(arr))
