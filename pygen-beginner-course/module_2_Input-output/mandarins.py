"""

Mandarins

n schoolchildren divide k mandarins equally, with the remaining indivisible mandarins left in the basket. How many whole mandarins will each schoolchild get? How many whole mandarins will remain in the basket?

Input Format
The program receives two integers as input: the number of schoolchildren and the number of mandarins, each on a separate line.

Output Format
The program should output two numbers: the number of mandarins that each schoolchild will get, and the number of mandarins that will remain in the basket, each on a separate line.
"""

n = int(input())
k = int(input())
a = k // n
b = k % n
print(a)
print(b)
