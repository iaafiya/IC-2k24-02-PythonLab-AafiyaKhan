# Snippet 19: Calculate power using recursion

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

result = power(base, exp)

print("Result:", result)

print("Time Complexity: O(exp)")
print("Space Complexity: O(exp)")
print("Justification: The exponent decreases by one in every recursive call, creating exp calls and stack frames.")
