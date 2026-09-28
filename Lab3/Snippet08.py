# Snippet 08: Print array elements and all possible pairs

arr = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(arr)

print("Individual elements:")

for i in range(n):
    print(arr[i])

print("All pairs:")

for j in range(n):
    for k in range(n):
        print(arr[j], arr[k])

print("Time Complexity: O(n^2)")
print("Justification: The first loop takes O(n), while the nested loops take O(n^2), so the total is O(n^2).")
