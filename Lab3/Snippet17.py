# Snippet 17: Check whether a string is a palindrome

s = input("Enter a string: ")

reversed_s = s[::-1]

if s == reversed_s:
    print("Palindrome: True")
else:
    print("Palindrome: False")

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
print("Justification: Reversing the string takes O(n) time and creates a new string of size n.")
