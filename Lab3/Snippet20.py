# Snippet 20: Calculate power using fast exponentiation

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

def fast_power(base, exp):
    if exp == 0:
        return 1

    half = fast_power(base, exp // 2)

    if exp % 2 == 0:
        return half * half

    return half * half * base

result = fast_power(base, exp)

print("Result:", result)

print("Time Complexity: O(log exp)")
print("Space Complexity: O(log exp)")
print("Justification: The exponent is divided by 2 at every recursive call, giving logarithmic time and recursion depth.")