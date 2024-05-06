"""
A sequence of numbers is called a geometric progression if each term, starting from the second one, is obtained by multiplying the previous term by the same constant number q (the common ratio).

If the first term of the progression and the common ratio are known, the n-th term of the geometric progression is found by the formula:

bn = b1 * q^(n-1)

Input:
The program receives three integers: b_1, q, and n, each on a separate line.

Output:
The program should output the n-th term of the geometric progression.

"""

b1 = int(input())
q = int(input())
n = int(input())
bn = b1 * q ** (n - 1)
print(bn)
