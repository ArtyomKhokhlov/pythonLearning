"""
Write a program that calculates the volume of a cube and the area of its total surface area based on the input value of the edge length.

Input Format
The program receives a single integer - the length of the edge.

Output Format
The program should output text and numbers in accordance with the task requirements.

Note 1. The volume of a cube and the total surface area can be calculated using the formulas:

V=a^3

S=6a^2
 

Note 2. Please note that at this stage of learning, we do not know about the exponentiation operator, so we use the definition of the power of a number – the number is multiplied by itself the specified number of times. For example:

a^4=a*a*a*a
"""

print("Enter edge length")
a = int(input())
v = a * a * a
s = 6 * a * a
print("Volume =", v)
print("Total surface area =", s)
