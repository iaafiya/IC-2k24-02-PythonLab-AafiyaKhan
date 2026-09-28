# Snippet 22: Build a frequency map of elements in an array

arr = list(map(int, input("Enter numbers separated by space: ").split()))

freq = {}

for val in arr:
    freq[val] = freq.get(val, 0) + 1

print("Frequency map:", freq)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
print("Justification: Each element is processed once and the dictionary can store up to n different values.")
