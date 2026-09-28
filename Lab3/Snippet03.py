# Snippet 03: Calculate the sum of digits of a number using recursion

n = int(input("Enter a number: "))

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

result = sum_digits(abs(n))

print("Sum of digits:", result)

print("Time Complexity: O(d)")
print("Space Complexity: O(d)")
print("Justification: The function processes one digit per recursive call, where d is the number of digits.")
