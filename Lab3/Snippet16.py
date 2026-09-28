# Snippet 16: Merge two sorted arrays into one sorted array

a = list(map(int, input("Enter first sorted array: ").split()))
b = list(map(int, input("Enter second sorted array: ").split()))

result = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print("Merged array:", result)

print("Time Complexity: O(m + n)")
print("Space Complexity: O(m + n)")
print("Justification: Each element from both arrays is processed once and stored in the result array.")
