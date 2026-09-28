# Snippet 06: Multiply two square matrices

n = int(input("Enter matrix size: "))

print("Enter first matrix:")
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

print("Enter second matrix:")
b = []

for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += a[i][k] * b[k][j]

print("Result matrix:")

for row in result:
    print(row)

print("Time Complexity: O(n^3)")
print("Space Complexity: O(n^2)")
print("Justification: Three nested loops perform n^3 multiplications and the result matrix requires n^2 space.")
