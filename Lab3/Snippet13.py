# Snippet 13: Calculate Fibonacci number using recursion

n = int(input("Enter n: "))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(n)

print("Fibonacci value:", result)

print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")
print("Justification: Each call creates two recursive calls, producing exponential time, while the maximum recursion depth is n.")
