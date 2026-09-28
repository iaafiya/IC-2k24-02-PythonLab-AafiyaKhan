# Snippet 02: Check whether an array contains duplicate elements

arr = list(map(int, input("Enter numbers separated by space: ").split()))

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            found = True
            break
    if found:
        break

print("Contains duplicate:", found)

print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print("Justification: Two nested loops compare pairs of elements, while no extra data structure is used.")
