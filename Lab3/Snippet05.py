# Snippet 05: Search for an element using binary search

arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter target value: "))

low = 0
high = len(arr) - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        result = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("Index:", result)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")
print("Justification: Each iteration cuts the search range approximately in half and uses constant extra space.")