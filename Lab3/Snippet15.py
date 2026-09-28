# Snippet 15: Generate and print all subsets of an array

arr = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(arr)

for i in range(2 ** n):
    subset = []

    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])

    print(subset)

print("Time Complexity: O(n * 2^n)")
print("Justification: There are 2^n subsets and each subset checks n elements.")
