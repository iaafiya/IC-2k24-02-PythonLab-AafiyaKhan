# Snippet 18: Convert a matrix into a one-dimensional list

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")

for i in range(m):
    matrix.append(list(map(int, input().split())))

flat = []

for row in matrix:
    for val in row:
        flat.append(val)

print("Flattened matrix:", flat)

print("Time Complexity: O(m*n)")
print("Space Complexity: O(m*n)")
print("Justification: Every matrix element is visited once and all m*n elements are stored in the new list.")
