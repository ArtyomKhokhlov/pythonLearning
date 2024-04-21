"""
Arithmetic Progression
An arithmetic progression is a sequence of numbers a1, a2, ..., an,
each of which, starting from a2, is obtained from the previous one by adding the same constant number d (the common difference).
Example of an arithmetic progression:
-6, -3, 0, 3, 6, 9, 12

If the first term of the progression (a1) and the common difference (d) are known,
the n-th term of the arithmetic progression is found using the formula:
an = a1 + d * (n - 1)

Input
The program receives three integers as input: a1, d, and n, each on a separate line.

Output
The program should output the n-th term of the arithmetic progression.
"""

a1 = int(input())
d = int(input())
n = int(input())
print(a1 + d * (n - 1))
