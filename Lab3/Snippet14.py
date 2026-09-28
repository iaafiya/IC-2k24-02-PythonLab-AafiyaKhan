# Snippet 14: Count pairs whose sum equals the target

arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))

seen = set()
count = 0

for num in arr:
    if target - num in seen:
        count += 1
    seen.add(num)

print("Number of pairs:", count)

print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
print("Justification: Each element is processed once using average O(1) set operations, and the set can contain n elements.")
