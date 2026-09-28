# Lab 3 – Time and Space Complexity

This lab contains 22 Python programs demonstrating different algorithms and their **time and space complexities**.

---

## Snippet 01 – Find Maximum Element

### Aim

To find the maximum element in an array and analyze its time and space complexity.

### Logic

The program stores the first element as the maximum value.
It then compares every remaining element with the current maximum and updates it when a larger value is found.

### Sample Input / Output

**Input:**

```text
10 25 7 40 15
```

**Output:**

```text
Maximum value: 40
Time Complexity: O(n)
Space Complexity: O(1)
Justification: The loop checks each element once and uses only one extra variable.
```

---

## Snippet 02 – Check Duplicate Elements

### Aim

To check whether an array contains any duplicate elements.

### Logic

The program compares each element with all elements that come after it.
If two elements are equal, a duplicate is found.

### Sample Input / Output

**Input:**

```text
1 2 3 4 2
```

**Output:**

```text
Contains duplicate: True
Time Complexity: O(n^2)
Space Complexity: O(1)
Justification: Two nested loops compare pairs of elements, while no extra data structure is used.
```

---

## Snippet 03 – Sum of Digits

### Aim

To calculate the sum of digits of a number using recursion.

### Logic

The last digit is obtained using the modulo operation.
The remaining number is passed recursively until the number becomes zero.

### Sample Input / Output

**Input:**

```text
12345
```

**Output:**

```text
Sum of digits: 15
Time Complexity: O(d)
Space Complexity: O(d)
Justification: The function processes one digit per recursive call, where d is the number of digits.
```

---

## Snippet 04 – Generate All Pairs

### Aim

To generate all possible pairs of elements from an array.

### Logic

Two nested loops are used to select every possible combination of two elements.
Each pair is stored in a result list.

### Sample Input / Output

**Input:**

```text
1 2 3
```

**Output:**

```text
All pairs:
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
(3, 1)
(3, 2)
(3, 3)
Time Complexity: O(n^2)
Space Complexity: O(n^2)
Justification: Two nested loops generate n^2 pairs and the result list stores all of them.
```

---

## Snippet 05 – Binary Search

### Aim

To search for an element in a sorted array using binary search.

### Logic

The program checks the middle element of the search range.
Depending on the comparison, half of the search range is eliminated in every iteration.

### Sample Input / Output

**Input:**

```text
10 20 30 40 50
30
```

**Output:**

```text
Index: 2
Time Complexity: O(log n)
Space Complexity: O(1)
Justification: Each iteration cuts the search range approximately in half and uses constant extra space.
```

---

## Snippet 06 – Matrix Multiplication

### Aim

To multiply two square matrices using three nested loops.

### Logic

The program calculates each element of the result matrix by multiplying corresponding elements of the two input matrices.
Three nested loops are used for rows, columns, and multiplication.

### Sample Input / Output

**Input:**

```text
2
1 2
3 4
5 6
7 8
```

**Output:**

```text
Result matrix:
[19, 22]
[43, 50]
Time Complexity: O(n^3)
Space Complexity: O(n^2)
Justification: Three nested loops perform n^3 multiplications and the result matrix requires n^2 space.
```

---

## Snippet 07 – Sparse Matrix

### Aim

To convert a matrix into sparse matrix triplet representation.

### Logic

The program checks every element of the matrix.
Only non-zero elements are stored as a tuple containing their row, column, and value.

### Sample Input / Output

**Input:**

```text
3
3
0 5 0
0 0 8
2 0 0
```

**Output:**

```text
Sparse matrix triplets:
(0, 1, 5)
(1, 2, 8)
(2, 0, 2)
Time Complexity: O(m*n)
Space Complexity: O(k)
Justification: Every matrix element is checked once, while only k non-zero elements are stored.
```

---

## Snippet 08 – Process Array and Print Pairs

### Aim

To print all elements of an array and all possible pairs of its elements.

### Logic

The first loop prints every element once.
The two nested loops then print every possible pair, which takes more time than the first loop.

### Sample Input / Output

**Input:**

```text
1 2 3
```

**Output:**

```text
Individual elements:
1
2
3
All pairs:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
Time Complexity: O(n^2)
```

---

## Snippet 09 – Check First Ten Values

### Aim

To check whether an array contains a value from 0 to 9.

### Logic

For every array element, the program compares it with numbers from 0 to 9.
Since the inner loop always runs only 10 times, it is considered constant time.

### Sample Input / Output

**Input:**

```text
15 20 25 7
```

**Output:**

```text
Contains a number from 0 to 9: True
Time Complexity: O(n)
Justification: The inner loop always runs at most 10 times, which is constant, so the overall complexity is O(n).
```

---

## Snippet 10 – Reverse Array Using New Array

### Aim

To reverse an array by creating a new array.

### Logic

The program starts from the last element and moves toward the first element.
Each element is appended to a new array in reverse order.

### Sample Input / Output

**Input:**

```text
1 2 3 4 5
```

**Output:**

```text
Reversed array: [5, 4, 3, 2, 1]
Time Complexity: O(n)
Space Complexity: O(n)
Justification: Every element is visited once and a new array stores all n elements.
```

---

## Snippet 11 – Reverse Array In Place

### Aim

To reverse an array without using an additional array.

### Logic

Two pointers are placed at the beginning and end of the array.
The elements at these positions are swapped while the pointers move toward the center.

### Sample Input / Output

**Input:**

```text
1 2 3 4 5
```

**Output:**

```text
Reversed array: [5, 4, 3, 2, 1]
Time Complexity: O(n)
Space Complexity: O(1)
Justification: The array is reversed in place using only two variables.
```

---

## Snippet 12 – Factorial Using Recursion

### Aim

To calculate the factorial of a number using recursion.

### Logic

The factorial function calls itself with `n - 1` until it reaches 0 or 1.
The recursive results are multiplied to obtain the final factorial.

### Sample Input / Output

**Input:**

```text
5
```

**Output:**

```text
Factorial: 120
Time Complexity: O(n)
Space Complexity: O(n)
Justification: There are n recursive calls and each call remains on the recursion stack.
```

---

## Snippet 13 – Fibonacci Using Recursion

### Aim

To calculate the nth Fibonacci number using recursive calls.

### Logic

The program recursively calculates the previous two Fibonacci numbers.
Each call creates two more calls until the base cases are reached.

### Sample Input / Output

**Input:**

```text
6
```

**Output:**

```text
Fibonacci value: 8
Time Complexity: O(2^n)
Space Complexity: O(n)
Justification: Each call creates two recursive calls, producing exponential time, while the maximum recursion depth is n.
```

---

## Snippet 14 – Count Pairs With Given Sum

### Aim

To count the number of pairs whose sum is equal to a given target.

### Logic

A set stores previously visited numbers.
For every number, the program checks whether its required complement is already present in the set.

### Sample Input / Output

**Input:**

```text
1 2 3 4 5
5
```

**Output:**

```text
Number of pairs: 2
Time Complexity: O(n)
Space Complexity: O(n)
Justification: Each element is processed once using average O(1) set operations, and the set can contain n elements.
```

---

## Snippet 15 – Print All Subsets

### Aim

To generate and print all possible subsets of an array.

### Logic

There are `2^n` possible subsets for an array of `n` elements.
Each binary representation from 0 to `2^n - 1` is used to determine which elements belong to a subset.

### Sample Input / Output

**Input:**

```text
1 2 3
```

**Output:**

```text
[]
[1]
[2]
[1, 2]
[3]
[1, 3]
[2, 3]
[1, 2, 3]
Time Complexity: O(n * 2^n)
Justification: There are 2^n subsets and each subset checks n elements.
```

---

## Snippet 16 – Merge Sorted Arrays

### Aim

To merge two sorted arrays into a single sorted array.

### Logic

Two pointers are used to compare elements from both arrays.
The smaller element is added to the result until all elements from both arrays are processed.

### Sample Input / Output

**Input:**

```text
1 3 5
2 4 6
```

**Output:**

```text
Merged array: [1, 2, 3, 4, 5, 6]
Time Complexity: O(m + n)
Space Complexity: O(m + n)
Justification: Each element from both arrays is processed once and stored in the result array.
```

---

## Snippet 17 – Check Palindrome

### Aim

To check whether a given string is a palindrome.

### Logic

The program creates the reverse of the string using slicing.
It compares the original string with the reversed string to determine whether it is a palindrome.

### Sample Input / Output

**Input:**

```text
madam
```

**Output:**

```text
Palindrome: True
Time Complexity: O(n)
Space Complexity: O(n)
Justification: Reversing the string takes O(n) time and creates a new string of size n.
```

---

## Snippet 18 – Flatten Matrix

### Aim

To convert a two-dimensional matrix into a one-dimensional list.

### Logic

Nested loops visit every row and every element in each row.
Each element is appended to a new one-dimensional list.

### Sample Input / Output

**Input:**

```text
2
3
1 2 3
4 5 6
```

**Output:**

```text
Flattened matrix: [1, 2, 3, 4, 5, 6]
Time Complexity: O(m*n)
Space Complexity: O(m*n)
Justification: Every matrix element is visited once and all m*n elements are stored in the new list.
```

---

## Snippet 19 – Power Using Recursion

### Aim

To calculate the power of a number using recursion.

### Logic

The function multiplies the base by itself recursively while decreasing the exponent by one.
The recursion stops when the exponent becomes zero.

### Sample Input / Output

**Input:**

```text
2
5
```

**Output:**

```text
Result: 32
Time Complexity: O(exp)
Space Complexity: O(exp)
Justification: The exponent decreases by one in every recursive call, creating exp calls and stack frames.
```

---

## Snippet 20 – Fast Power

### Aim

To calculate the power of a number using fast exponentiation.

### Logic

The exponent is divided by 2 during every recursive call.
The result of the smaller problem is squared, making the algorithm much faster than normal recursive power.

### Sample Input / Output

**Input:**

```text
2
10
```

**Output:**

```text
Result: 1024
Time Complexity: O(log exp)
Space Complexity: O(log exp)
Justification: The exponent is divided by 2 at every recursive call, giving logarithmic time and recursion depth.
```

---

## Snippet 21 – Check Common Element

### Aim

To check whether two arrays contain at least one common element.

### Logic

Every element of the first array is compared with every element of the second array.
If two equal elements are found, the program returns true.

### Sample Input / Output

**Input:**

```text
1 2 3 4
7 8 3 9
```

**Output:**

```text
Has common element: True
Time Complexity: O(m*n)
Space Complexity: O(1)
Justification: Every element of array a may be compared with every element of array b, using constant extra space.
```

---

## Snippet 22 – Build Frequency Map

### Aim

To count the frequency of each element in an array.

### Logic

A dictionary is used to store each unique value and its count.
For every element, its existing count is increased or a new count of 1 is created.

### Sample Input / Output

**Input:**

```text
1 2 2 3 3 3 4
```

**Output:**

```text
Frequency map: {1: 1, 2: 2, 3: 3, 4: 1}
Time Complexity: O(n)
Space Complexity: O(n)
Justification: Each element is processed once and the dictionary can store up to n different values.
```

---

# Summary of Complexities

| Snippet | Program               | Time Complexity | Space Complexity |
| ------- | --------------------- | --------------- | ---------------- |
| 01      | Find Maximum          | O(n)            | O(1)             |
| 02      | Check Duplicate       | O(n²)           | O(1)             |
| 03      | Sum of Digits         | O(d)            | O(d)             |
| 04      | Generate Pairs        | O(n²)           | O(n²)            |
| 05      | Binary Search         | O(log n)        | O(1)             |
| 06      | Matrix Multiplication | O(n³)           | O(n²)            |
| 07      | Sparse Matrix         | O(m × n)        | O(k)             |
| 08      | Process Array         | O(n²)           | O(1)             |
| 09      | Check First Ten       | O(n)            | O(1)             |
| 10      | Reverse New Array     | O(n)            | O(n)             |
| 11      | Reverse In Place      | O(n)            | O(1)             |
| 12      | Factorial             | O(n)            | O(n)             |
| 13      | Fibonacci             | O(2ⁿ)           | O(n)             |
| 14      | Count Pairs           | O(n)            | O(n)             |
| 15      | All Subsets           | O(n × 2ⁿ)       | O(n)             |
| 16      | Merge Sorted Arrays   | O(m + n)        | O(m + n)         |
| 17      | Palindrome            | O(n)            | O(n)             |
| 18      | Flatten Matrix        | O(m × n)        | O(m × n)         |
| 19      | Power                 | O(exp)          | O(exp)           |
| 20      | Fast Power            | O(log exp)      | O(log exp)       |
| 21      | Common Element        | O(m × n)        | O(1)             |
| 22      | Frequency Map         | O(n)            | O(n)             |

---

## Conclusion

These programs demonstrate different time and space complexity patterns, including constant, linear, logarithmic, quadratic, cubic, exponential, and logarithmic-recursive algorithms.
