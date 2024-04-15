"""
Write a program that reads an integer, then displays the next and previous integers with explanatory text.

Input Format
The program receives an integer as input.

Output Format
The program should display text according to the task's requirements.
"""

a = int(input())
b = a + 1
c = a - 1
print("The next number after", a, "is:", b)
print("The previous number for", a, "is:", c)
