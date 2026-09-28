# Snippet 07: Convert a matrix into sparse matrix triplet form

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix:")
for i in range(m):
    matrix.append(list(map(int, input().split())))

triples = []

for r in range(m):
    for c in range(n):
        if matrix[r][c] != 0:
            triples.append((r, c, matrix[r][c]))

print("Sparse matrix triplets:")

for triple in triples:
    print(triple)

k = len(triples)

print("Time Complexity: O(m*n)")
print("Space Complexity: O(k)")
print("Justification: Every matrix element is checked once, while only k non-zero elements are stored.")
