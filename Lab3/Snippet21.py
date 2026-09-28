# Snippet 21: Check whether two arrays have a common element

a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

found = False

for x in a:
    for y in b:
        if x == y:
            found = True
            break
    if found:
        break

print("Has common element:", found)

print("Time Complexity: O(m*n)")
print("Space Complexity: O(1)")
print("Justification: Every element of array a may be compared with every element of array b, using constant extra space.")
