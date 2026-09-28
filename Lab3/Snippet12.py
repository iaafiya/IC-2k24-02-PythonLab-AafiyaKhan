# Snippet 12: Calculate factorial using recursion

n = int(input("Enter a non-negative integer: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(n)

print("Factorial:", result)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
print("Justification: There are n recursive calls and each call remains on the recursion stack.")
