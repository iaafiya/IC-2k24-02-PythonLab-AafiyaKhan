# Snippet 09: Check whether an array contains a value from 0 to 9

arr = list(map(int, input("Enter numbers separated by space: ").split()))

found = False

for i in range(len(arr)):
    for j in range(10):
        if arr[i] == j:
            found = True
            break
    if found:
        break

print("Contains a number from 0 to 9:", found)

print("Time Complexity: O(n)")
print("Justification: The inner loop always runs at most 10 times, which is constant, so the overall complexity is O(n).")
