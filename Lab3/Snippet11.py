# Snippet 11: Reverse an array in place

arr = list(map(int, input("Enter numbers separated by space: ").split()))

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print("Justification: The array is traversed from both ends and no extra array is created.")
