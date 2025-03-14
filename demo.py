print("Hello ITL!")

arr = [20, 17, 45, 2, 34, 14, 12, 15, 27, 11]

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10   # Count array (0-9 digits)
    
    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so it contains actual position of this digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copy the output array to arr[], so that arr now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)  # Find the maximum number to determine number of digits
    exp = 1  # Start with the least significant digit
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

radix_sort(arr)
print("Sorted array:", arr)
