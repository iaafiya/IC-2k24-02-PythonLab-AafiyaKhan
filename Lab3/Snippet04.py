# Snippet 04: Generate all possible pairs from an array

arr = list(map(int, input("Enter numbers separated by space: ").split()))

result = []

n = len(arr)

for i in range(n):
    for j in range(n):
        result.append((arr[i], arr[j]))

print("All pairs:")

for pair in result:
    print(pair)

print("Time Complexity: O(n^2)")
print("Space Complexity: O(n^2)")
print("Justification: Two nested loops generate n^2 pairs and the result list stores all of them.")
