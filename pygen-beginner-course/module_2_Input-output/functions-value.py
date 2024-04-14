"""
The function's value is to be calculated by a program according to the following formula:

f(a, b) = 3(a + b)^3 + 275b^2 - 127a - 41

where a and b are integer values provided as input.

Input format:
The program receives two integers, each on a separate line. The first line contains the value of a, and the second line contains the value of b.

Output format:
The program should output the value of the function based on the input numbers a and b.

Note 1: Use the input() command to read the text and the print() command to print the text on the screen.

Note 2: Note that at this stage of learning, we do not know about the exponentiation operator, so we use the definition of the power of a number – the number is multiplied by itself the specified number of times.
"""

a = int(input())
b = int(input())
result = 3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41
print(result)
