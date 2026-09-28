# Snippet 10: Reverse an array using a new array

arr = list(map(int, input("Enter numbers separated by space: ").split()))

reversed_arr = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print("Reversed array:", reversed_arr)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
print("Justification: Every element is visited once and a new array stores all n elements.")
