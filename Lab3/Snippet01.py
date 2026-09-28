# Snippet 01: Find the maximum element in an array

arr = list(map(int, input("Enter numbers separated by space: ").split()))

max_val = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]

print("Maximum value:", max_val)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print("Justification: The loop checks each element once and uses only one extra variable.")
